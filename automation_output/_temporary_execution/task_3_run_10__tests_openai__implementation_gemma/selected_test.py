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
            {"weight": 7}
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
            {"score": 3.14159},
            {"score": 7},
            {"score": 2.718}
        ]
        attribute = "score"
        # Action
        result = get_min_2_attributes(data, attribute)
        # Verify
        self.assertEqual(result, 2.72)

    def test_ignore_products_without_attribute(self):
        # Setup
        data = [
            {"price": 10},
            {"cost": 5},
            {"price": 7},
            {"cost": 2}
        ]
        attribute = "price"
        # Action
        result = get_min_2_attributes(data, attribute)
        # Verify
        self.assertEqual(result, 7)

    def test_attribute_values_are_zero(self):
        # Setup
        data = [
            {"value": 0},
            {"value": 0.0},
            {"value": None},
            {"value": 1}
        ]
        attribute = "value"
        # Action
        result = get_min_2_attributes(data, attribute)
        # Verify
        self.assertEqual(result, 0.0)

    def test_attribute_values_all_none_and_missing(self):
        # Setup
        data = [
            {"attr": None},
            {"other": 5},
            {"attr": None},
            {"other": 2}
        ]
        attribute = "attr"
        # Action
        result = get_min_2_attributes(data, attribute)
        # Verify
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()