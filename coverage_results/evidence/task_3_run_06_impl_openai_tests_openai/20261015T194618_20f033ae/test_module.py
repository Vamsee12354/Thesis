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

    def test_all_values_none(self):
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
            {"weight": None},
            {"weight": 7}
        ]
        # Action & Verify
        self.assertEqual(get_min_2_attributes(data, "weight"), 5.56)

    def test_values_are_integers_and_floats(self):
        # Setup
        data = [
            {"score": 10},
            {"score": 5.1234},
            {"score": 7},
            {"score": 5.126}
        ]
        # Action & Verify
        self.assertEqual(get_min_2_attributes(data, "score"), 5.12)

    def test_ignore_products_without_attribute(self):
        # Setup
        data = [
            {"price": 10},
            {"cost": 5},
            {"price": 7},
            {"cost": 3}
        ]
        # Action & Verify
        self.assertEqual(get_min_2_attributes(data, "price"), 7)

    def test_attribute_values_are_not_numeric(self):
        # Setup
        data = [
            {"price": "10"},
            {"price": "5"},
            {"price": "7"}
        ]
        # Action & Verify
        self.assertIsNone(get_min_2_attributes(data, "price"))

    def test_rounding_of_minimum_value(self):
        # Setup
        data = [
            {"value": 1.234},
            {"value": 1.235},
            {"value": 1.236}
        ]
        # Action & Verify
        self.assertEqual(get_min_2_attributes(data, "value"), 1.23)

if __name__ == "__main__":
    unittest.main()