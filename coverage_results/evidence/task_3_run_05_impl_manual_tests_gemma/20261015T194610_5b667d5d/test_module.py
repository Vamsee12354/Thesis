import unittest
from implementation_manual import get_min_2_attributes

class TestGetMin2Attributes(unittest.TestCase):

    def test_happy_path_float_values(self):
        # Setup
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},
            {"battery_life": 2.0}
        ]
        search_key = "price"
        expected = 29.99

        # Action
        result = get_min_2_attributes(data, search_key)

        # Verification
        self.assertEqual(result, expected)

    def test_happy_path_integer_values(self):
        # Setup
        data = [
            {"weight": 10},
            {"weight": 5},
            {"weight": 15},
            {"weight": 7}
        ]
        search_key = "weight"
        expected = 5.0

        # Action
        result = get_min_2_attributes(data, search_key)

        # Verification
        self.assertEqual(result, expected)

    def test_rounding_to_two_decimals(self):
        # Setup
        data = [
            {"val": 10.555},
            {"val": 10.554},
            {"val": 10.556}
        ]
        search_key = "val"
        expected = 10.55

        # Action
        result = get_min_2_attributes(data, search_key)

        # Verification
        self.assertEqual(result, expected)

    def test_empty_list_returns_none(self):
        # Setup
        data = []
        search_key = "price"

        # Action
        result = get_min_2_attributes(data, search_key)

        # Verification
        self.assertIsNone(result)

    def test_non_existent_attribute_returns_none(self):
        # Setup
        data = [
            {"price": 49.99},
            {"battery_life": 3.5}
        ]
        search_key = "non_existent_field"

        # Action
        result = get_min_2_attributes(data, search_key)

        # Verification
        self.assertIsNone(result)

    def test_all_values_are_none_returns_none(self):
        # Setup
        data = [
            {"price": None},
            {"price": None},
            {"other": 10}
        ]
        search_key = "price"

        # Action
        result = get_min_2_attributes(data, search_key)

        # Verification
        self.assertIsNone(result)

    def test_mixed_missing_and_none_values(self):
        # Setup
        data = [
            {"price": 49.99},
            {"price": None},
            {"battery_life": 2.0},
            {"other": 10.0}
        ]
        search_key = "price"
        expected = 49.99

        # Action
        result = get_min_2_attributes(data, search_key)

        # Verification
        self.assertEqual(result, expected)

    def test_non_numeric_values_ignored(self):
        # Setup
        # The spec implies the attribute must be numeric. 
        # If a value is a string, it shouldn't be considered in min calculation.
        data = [
            {"price": 10.0},
            {"price": "expensive"},
            {"price": 5.0}
        ]
        search_key = "price"
        expected = 5.0

        # Action
        result = get_min_2_attributes(data, search_key)

        # Verification
        self.assertEqual(result, expected)

    def test_all_non_numeric_values_returns_none(self):
        # Setup
        data = [
            {"title": "A"},
            {"title": "B"},
            {"title": None}
        ]
        search_key = "title"

        # Action
        result = get_min_2_attributes(data, search_key)

        # Verification
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()