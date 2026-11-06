#!/usr/bin/env python3
"""Check documentation packaging, local links and the tested skill snapshot."""
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def main():
    failures = []
    index = ROOT / "docs/i18n"
    manifest = json.loads((index / "languages.json").read_text(encoding="utf-8"))
    languages = manifest["languages"]
    if len(languages) != 32 or len({x["code"] for x in languages}) != 32:
        failures.append("expected 32 unique language guides")
    if [x["rank"] for x in languages] != list(range(1, 33)):
        failures.append("selection order differs from manifest")
    paths = {index / x["path"] for x in languages}
    if paths != set(index.glob("*/README.md")):
        failures.append("manifest and translated Markdown files differ")
    for path in sorted(paths):
        if not path.exists():
            failures.append(f"missing guide: {path}")
            continue
        text = path.read_text(encoding="utf-8")
        if len(text.strip()) < 500 or text.count("$security-review ") != 3:
            failures.append(f"incomplete guide: {path}")
    markdown = [ROOT / "README.md", *index.rglob("*.md"),
                * (ROOT / "security-review").rglob("*.md"), ROOT / "evals/README.md"]
    links_checked = 0
    for path in markdown:
        if not path.exists():
            failures.append(f"missing document: {path}")
            continue
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            file_target = target.split("#", 1)[0]
            if not (path.parent / file_target).exists():
                failures.append(f"broken relative link: {path.relative_to(ROOT)} -> {target}")
            links_checked += 1
    snapshot = json.loads((ROOT / "evals/results/2026-11-05/skill-snapshot.json").read_text())
    snapshot_matches = all((ROOT / path).exists() and
        hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected
        for path, expected in snapshot["files"].items())
    result = {"language_guides": len(paths), "local_links_checked": links_checked,
              "snapshot_matches_current_skill": snapshot_matches,
              "checks_passed": not failures, "failures": failures,
              "limits": "Does not assess translation fluency or agent behavior."}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    # A changed skill is a warning: previous behavioral evidence does not validate new instructions.
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
