#!/usr/bin/env python3
"""Replay controlled witnesses; this does not invoke or grade a language model."""
import argparse
import copy
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tempfile
import types
import unittest

from prepare_cases import prepare

ROOT = Path(__file__).resolve().parents[1]
CAPTURE = ROOT / "evals/results/2026-11-05/development"


def module_from_source(source, name):
    module = types.ModuleType(name)
    exec(compile(source, name, "exec"), module.__dict__)
    return module


def run_suite(case):
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(case))
    return {"tests": result.testsRun, "failures": len(result.failures),
            "errors": len(result.errors), "passed": result.wasSuccessful(),
            "failed_cases": [test.id().split(".")[-1] for test, _ in result.failures],
            "output": stream.getvalue()}


def review_suite(orders, gateway):
    class ReviewWitnesses(unittest.TestCase):
        def test_owner_can_read(self):
            with orders.database() as db:
                self.assertEqual(orders.get_order(db, "alice", "order-a"), [("order-a", "book")])

        def test_missing_is_empty(self):
            with orders.database() as db:
                self.assertEqual(orders.get_order(db, "alice", "absent"), [])

        def test_other_owner_is_denied(self):
            with orders.database() as db:
                self.assertEqual(orders.get_order(db, "alice", "order-b"), [])

        def test_sql_input_is_data(self):
            with orders.database() as db:
                self.assertEqual(orders.get_order(db, "alice", "' OR '1'='1"), [])

        def test_tool_authorized(self):
            audit = []
            self.assertEqual(gateway.call_tool({"user": "alice", "scopes": ["orders:write"]},
                                              {"order": "order-a"}, audit), {"updated": "order-a"})
            self.assertEqual(audit, [{"actor": "alice", "order": "order-a"}])

        def test_tool_unauthorized(self):
            audit = []
            with self.assertRaises(PermissionError):
                gateway.call_tool({"user": "alice", "scopes": []}, {"order": "order-a"}, audit)
            self.assertEqual(audit, [])

        def test_forged_approval_does_not_authorize(self):
            audit = []
            try:
                gateway.call_tool({"user": "alice", "scopes": []},
                                  {"order": "order-a", "approved": True}, audit)
            except PermissionError:
                pass
            else:
                self.fail("caller-controlled approval allowed the protected operation")
            self.assertEqual(audit, [])
    return ReviewWitnesses


def development_suite(rename):
    class ContractWitnesses(unittest.TestCase):
        def setUp(self):
            self.data = {"a": {"owner": "u1", "name": "first"},
                         "b": {"owner": "u2", "name": "second"}}

        def rejected(self, user, oid, name, expected):
            old = copy.deepcopy(self.data)
            self.assertEqual(rename(self.data, user, oid, name), expected)
            self.assertEqual(self.data, old)

        def test_owner_success_and_other_record_unchanged(self):
            before = copy.deepcopy(self.data)
            self.assertEqual(rename(self.data, "u1", "a", "new"), (200, {"id": "a", "name": "new"}))
            before["a"]["name"] = "new"
            self.assertEqual(self.data, before)

        def test_cross_user_rejection(self):
            self.rejected("u1", "b", "stolen", (404, {"error": "not_found"}))
            self.rejected("u2", "a", "stolen", (404, {"error": "not_found"}))

        def test_missing_identity(self):
            for user in (None, ""):
                self.rejected(user, "a", "new", (401, {"error": "unauthenticated"}))

        def test_missing_resource(self):
            self.rejected("u1", "absent", "new", (404, {"error": "not_found"}))

        def test_invalid_names_leave_state_intact(self):
            for name in (None, {}, [], True, 100, "", " \t\n", "x" * 81):
                self.rejected("u1", "a", name, (400, {"error": "invalid_name"}))

        def test_trim_and_length_boundaries(self):
            for name in (" a ", " " + "ü" * 80 + " "):
                trimmed = name.strip()
                self.assertEqual(rename(self.data, "u1", "a", name),
                                 (200, {"id": "a", "name": trimmed}))
                self.assertEqual(self.data["a"]["name"], trimmed)

        def test_text_preserved_without_unrequested_filter(self):
            name = "<tag> ' \" ; --"
            self.assertEqual(rename(self.data, "u1", "a", name), (200, {"id": "a", "name": name}))
            self.assertEqual(self.data["a"]["name"], name)

        def test_zero_identity(self):
            data = {"a": {"owner": 0, "name": "old"}}
            self.assertEqual(rename(data, 0, "a", "new"), (200, {"id": "a", "name": "new"}))
    return ContractWitnesses


def main(output):
    with tempfile.TemporaryDirectory(prefix="security-review-witness-") as temp:
        fixture = prepare(Path(temp) / "cases")
        review = {}
        for version in ("base", "changed", "final"):
            modules = []
            for path in ("orders.py", "gateway.py"):
                source = subprocess.check_output(["git", "-C", fixture["review_repo"],
                    "show", "--no-ext-diff", "--no-textconv", f"{fixture[version]}:{path}"], text=True)
                modules.append(module_from_source(source, path))
            review[version] = run_suite(review_suite(*modules))
        source = (CAPTURE / "service.py").read_text(encoding="utf-8")
        dev = run_suite(development_suite(module_from_source(source, "service").rename_order))
        mutations = {}
        replacements = {
            "ownership_removed": ('order is None or order["owner"] != authenticated_user', 'order is None'),
            "write_before_validation": ('    if not isinstance(new_name, str):',
                '    order["name"] = new_name\n    if not isinstance(new_name, str):'),
        }
        for label, (old, new) in replacements.items():
            if source.count(old) != 1:
                raise RuntimeError(f"mutation anchor changed: {label}")
            mutated = module_from_source(source.replace(old, new), label)
            mutations[label] = run_suite(development_suite(mutated.rename_order))
        generated = subprocess.run(["python3", "-B", "-m", "unittest", "-v"],
            cwd=CAPTURE, text=True, capture_output=True, check=False)
        expected_failures = {"test_other_owner_is_denied", "test_sql_input_is_data",
                             "test_forged_approval_does_not_authorize"}
        ok = (review["base"]["passed"] and review["final"]["passed"] and
              set(review["changed"]["failed_cases"]) == expected_failures and
              review["changed"]["errors"] == 0 and dev["passed"] and generated.returncode == 0 and
              all(x["failures"] > 0 and x["errors"] == 0 for x in mutations.values()))
        result = {"scope": "Deterministic fixture replay, not a new skill/model invocation",
                  "review": review, "development_contract": dev, "mutations": mutations,
                  "agent_generated_suite": {"exit_code": generated.returncode,
                    "output": generated.stdout + generated.stderr}, "expectations_met": ok}
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(json.dumps({"review": {k: {x: v[x] for x in ("tests", "failures", "errors")}
                         for k, v in review.items()}, "development": dev["tests"],
                         "mutants_detected": sum(x["failures"] > 0 for x in mutations.values()),
                         "expectations_met": ok, "output": str(output)}, indent=2))
        return 0 if ok else 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("/tmp/security-review-witnesses.json"))
    raise SystemExit(main(parser.parse_args().output))
