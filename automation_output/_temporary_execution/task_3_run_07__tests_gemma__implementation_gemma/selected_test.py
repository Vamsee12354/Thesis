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

    def test_battery_life_minimum(self):
        # Setup
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},
            {"battery_life": 2.0}
        ]
        search_key = "battery_life"
        expected = 2.0

        # Action
        result = get_min_2_attributes(data, search_key)

        # Verification
        self.assertEqual(result, expected)

    def test_rounding_to_two_decimals(self):
        # Setup
        data = [
            {"val": 10.1234},
            {"val": 10.1267},
            {"val": 10.1211}
        ]
        search_key = "val"
        expected = 10.12

        # Action
        result = get_min_2_attributes(data, search_key)

        # Verification
        self.assertEqual(result, expected)

    def test_non_existent_field(self):
        # Setup
        data = [
            {"price": 49.99},
            {"battery_life": 4.0}
        ]
        search_key = "non_existent_field"
        expected = None

        # Action
        result = get_min_2_attributes(data, search_key)

        # Verification
        self.assertIsNone(result)

    def test_empty_list(self):
        # Setup
        data = []
        search_key = "price"
        expected = None

        # Action
        result = get_min_2_attributes(data, search_key)

        # Verification
        self.assertIsNone(result)

    def test_all_values_are_none(self):
        # Setup
        data = [
            {"price": None},
            {"price": None},
            {"other": 10}
        ]
        search_key = "price"
        expected = None

        # Action
        result = get_min_2_attributes(data, search_key)

        # Verification
        self.assertIsNone(result)

    def test_non_numeric_values(self):
        # Setup
        # The spec implies non-numeric values should be ignored or result in None 
        # if they can't be compared.
        data = [
            {"title": "A"},
            {"title": "B"},
            {"title": "C"},
            {"title": None}
        ]
        search_key = "title"
        expected = None

        # Action
        result = get_min_2_attributes(data, search_key)

        # Verification
        self.assertIsNone(result)

    def test_mixed_presence_of_attribute(self):
        # Setup
        data = [
            {"val": 10.5},
            {"other": 5.0},
            {"val": 2.5},
            {"val": None}
        ]
        search_key = "val"
        expected = 2.5

        # Action
        result = get_min_2_attributes(data, search_key)

        # Verification
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()