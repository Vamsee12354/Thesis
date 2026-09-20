import unittest
from implementation_manual import get_min_2_attributes

class TestGetMin2Attributes(unittest.TestCase):

    def test_minimum_value_with_valid_numeric_attribute(self):
        # Setup
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},
            {"battery_life": 2.0}
        ]
        attribute = "price"
        # Action
        result = get_min_2_attributes(data, attribute)
        # Verify
        self.assertEqual(result, 29.99)

    def test_minimum_value_with_another_valid_numeric_attribute(self):
        # Setup
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},
            {"battery_life": 2.0}
        ]
        attribute = "battery_life"
        # Action
        result = get_min_2_attributes(data, attribute)
        # Verify
        self.assertEqual(result, 2.0)

    def test_attribute_not_present_in_any_product(self):
        # Setup
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},
            {"battery_life": 2.0}
        ]
        attribute = "non_existent_field"
        # Action
        result = get_min_2_attributes(data, attribute)
        # Verify
        self.assertIsNone(result)

    def test_all_values_none_for_attribute(self):
        # Setup
        data = [
            {"title": "A"},
            {"title": "B"},
            {"title": "C"},
            {"title": None}
        ]
        attribute = "title"
        # Action
        result = get_min_2_attributes(data, attribute)
        # Verify
        self.assertIsNone(result)

    def test_empty_data_list(self):
        # Setup
        data = []
        attribute = "price"
        # Action
        result = get_min_2_attributes(data, attribute)
        # Verify
        self.assertIsNone(result)

    def test_mixed_none_and_numeric_values(self):
        # Setup
        data = [
            {"weight": None},
            {"weight": 10},
            {"weight": 5.555},
            {"weight": None},
            {"weight": 7.1}
        ]
        attribute = "weight"
        # Action
        result = get_min_2_attributes(data, attribute)
        # Verify
        self.assertEqual(result, 5.56)

    def test_integer_and_float_values(self):
        # Setup
        data = [
            {"size": 10},
            {"size": 3.14159},
            {"size": 7},
            {"size": 3.14}
        ]
        attribute = "size"
        # Action
        result = get_min_2_attributes(data, attribute)
        # Verify
        self.assertEqual(result, 3.14)

    def test_ignore_products_without_attribute(self):
        # Setup
        data = [
            {"price": 20},
            {"cost": 10},
            {"price": 15},
            {"cost": 5}
        ]
        attribute = "price"
        # Action
        result = get_min_2_attributes(data, attribute)
        # Verify
        self.assertEqual(result, 15)

    def test_rounding_of_minimum_value(self):
        # Setup
        data = [
            {"value": 1.234},
            {"value": 1.235},
            {"value": 1.236}
        ]
        attribute = "value"
        # Action
        result = get_min_2_attributes(data, attribute)
        # Verify
        self.assertEqual(result, 1.23)

    def test_non_numeric_values_ignored(self):
        # Setup
        data = [
            {"attr": "string"},
            {"attr": None},
            {"attr": 5},
            {"attr": 3.5}
        ]
        attribute = "attr"
        # Action
        result = get_min_2_attributes(data, attribute)
        # Verify
        self.assertEqual(result, 3.5)

if __name__ == "__main__":
    unittest.main()