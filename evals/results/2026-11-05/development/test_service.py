import copy
import unittest

from service import rename_order


class RenameOrderTests(unittest.TestCase):
    def setUp(self):
        self.orders = {
            "order-a": {"owner": "alice", "name": "Original A"},
            "order-b": {"owner": "bob", "name": "Private B"},
        }

    def assert_rejected(self, user, order_id, name, expected):
        before = copy.deepcopy(self.orders)
        result = rename_order(self.orders, user, order_id, name)
        # Check effects before the response so even a rejection after a write fails.
        self.assertEqual(self.orders, before)
        self.assertEqual(result, expected)

    def test_owner_renames_only_selected_order(self):
        result = rename_order(self.orders, "alice", "order-a", "New name")
        self.assertEqual(result, (200, {"id": "order-a", "name": "New name"}))
        self.assertEqual(self.orders, {
            "order-a": {"owner": "alice", "name": "New name"},
            "order-b": {"owner": "bob", "name": "Private B"},
        })

    def test_trims_name_before_saving_and_returning(self):
        result = rename_order(self.orders, "alice", "order-a", " \t Café  de Ana \n")
        self.assertEqual(result, (200, {"id": "order-a", "name": "Café  de Ana"}))
        self.assertEqual(self.orders["order-a"]["name"], "Café  de Ana")

    def test_accepts_trimmed_length_boundaries(self):
        for name in ("x", "á" * 80, "  " + "x" * 80 + "  "):
            with self.subTest(name=name):
                self.assertEqual(rename_order(self.orders, "alice", "order-a", name),
                                 (200, {"id": "order-a", "name": name.strip()}))
                self.assertEqual(self.orders["order-a"]["name"], name.strip())

    def test_missing_identity_has_no_effect(self):
        for user in (None, ""):
            for order_id in ("order-a", "order-b", "missing"):
                with self.subTest(user=user, order_id=order_id):
                    self.assert_rejected(user, order_id, "New", (401, {"error": "unauthenticated"}))

    def test_other_owner_cannot_rename_by_changing_identifier(self):
        self.assert_rejected("alice", "order-b", "Takeover", (404, {"error": "not_found"}))
        self.assert_rejected("bob", "order-a", "Takeover", (404, {"error": "not_found"}))

    def test_missing_order_matches_other_owner_response(self):
        self.assert_rejected("alice", "missing", "New", (404, {"error": "not_found"}))

    def test_rejects_non_string_names_without_coercion(self):
        for name in (None, True, 0, 12.5, b"name", ["name"], {"name": "new", "owner": "alice"}):
            with self.subTest(name=name):
                self.assert_rejected("alice", "order-a", name, (400, {"error": "invalid_name"}))

    def test_rejects_empty_blank_and_oversized_names(self):
        for name in ("", "  \t\n", "\u2003\u00a0", "x" * 81, "  " + "x" * 81 + " "):
            with self.subTest(name=name):
                self.assert_rejected("alice", "order-a", name, (400, {"error": "invalid_name"}))

    def test_auth_and_ownership_take_precedence_over_invalid_name(self):
        self.assert_rejected(None, "order-a", {}, (401, {"error": "unauthenticated"}))
        self.assert_rejected("alice", "order-b", {}, (404, {"error": "not_found"}))
        self.assert_rejected("alice", "missing", {}, (404, {"error": "not_found"}))

    def test_text_is_preserved_as_data(self):
        name = "<script>alert(1)</script> ' ; --"
        result = rename_order(self.orders, "alice", "order-a", name)
        self.assertEqual(result, (200, {"id": "order-a", "name": name}))
        self.assertEqual(self.orders["order-a"]["name"], name)

    def test_zero_is_a_valid_identity(self):
        orders = {7: {"owner": 0, "name": "Original"}}
        self.assertEqual(rename_order(orders, 0, 7, "New"), (200, {"id": 7, "name": "New"}))
        self.assertEqual(orders, {7: {"owner": 0, "name": "New"}})


if __name__ == "__main__":
    unittest.main()
