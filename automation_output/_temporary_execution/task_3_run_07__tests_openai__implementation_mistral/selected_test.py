import unittest
from implementation_manual import get_min_2_attributes

class TestGetMin2Attributes(unittest.TestCase):

    def test_minimum_value_present(self):
        # Setup
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},
            {"battery_life": 2.0}
        ]
        # Action & Verify
        self.assertEqual(get_min_2_attributes(data, "price"), 29.99)
        self.assertEqual(get_min_2_attributes(data, "battery_life"), 2.0)

    def test_attribute_not_present_in_any_product(self):
        # Setup
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},
            {"battery_life": 2.0}
        ]
        # Action & Verify
        self.assertIsNone(get_min_2_attributes(data, "non_existent_field"))

    def test_all_values_none_for_attribute(self):
        # Setup
        data = [
            {"title": "A"},
            {"title": "B"},
            {"title": "C"},
            {"title": None}
        ]
        # Action & Verify
        self.assertIsNone(get_min_2_attributes(data, "title"))

    def test_empty_data_list(self):
        # Setup
        data = []
        # Action & Verify
        self.assertIsNone(get_min_2_attributes(data, "price"))

    def test_mixed_none_and_numeric_values(self):
        # Setup
        data = [
            {"weight": None},
            {"weight": 10},
            {"weight": 5.555},
            {"weight": None}
        ]
        # Action & Verify
        self.assertEqual(get_min_2_attributes(data, "weight"), 5.56)

    def test_integer_and_float_values(self):
        # Setup
        data = [
            {"score": 10},
            {"score": 5.5},
            {"score": 7},
            {"score": 5}
        ]
        # Action & Verify
        self.assertEqual(get_min_2_attributes(data, "score"), 5.0)

    def test_ignore_products_without_attribute(self):
        # Setup
        data = [
            {"price": 20},
            {"cost": 10},
            {"price": 15},
            {"cost": 5}
        ]
        # Action & Verify
        self.assertEqual(get_min_2_attributes(data, "price"), 15.0)

    def test_rounding_to_two_decimals(self):
        # Setup
        data = [
            {"value": 1.234},
            {"value": 1.235},
            {"value": 1.236}
        ]
        # Action & Verify
        self.assertEqual(get_min_2_attributes(data, "value"), 1.23)

    def test_non_numeric_values_ignored(self):
        # Setup
        data = [
            {"attr": "string"},
            {"attr": None},
            {"attr": 10},
            {"attr": 5}
        ]
        # Action & Verify
        self.assertEqual(get_min_2_attributes(data, "attr"), 5.0)

    def test_all_non_numeric_or_none_values(self):
        # Setup
        data = [
            {"attr": "string"},
            {"attr": None},
            {"attr": "another string"}
        ]
        # Action & Verify
        self.assertIsNone(get_min_2_attributes(data, "attr"))

if __name__ == "__main__":
    unittest.main()