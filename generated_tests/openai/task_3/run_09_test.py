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
            {"score": 10},
            {"score": 5.1234},
            {"score": 7},
            {"score": 5.126}
        ]
        attribute = "score"
        # Action
        result = get_min_2_attributes(data, attribute)
        # Verify
        self.assertEqual(result, 5.12)

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

    def test_attribute_values_are_not_numeric(self):
        # Setup
        data = [
            {"price": "cheap"},
            {"price": "expensive"},
            {"price": None}
        ]
        attribute = "price"
        # Action
        result = get_min_2_attributes(data, attribute)
        # Verify
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()