from implementation_manual import get_min_2_attributes
import unittest

class TestGetMin2Attributes(unittest.TestCase):

    def test_happy_path_price(self):
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},
            {"battery_life": 2.0}
        ]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, 29.99)

    def test_happy_path_battery_life(self):
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},
            {"battery_life": 2.0}
        ]
        result = get_min_2_attributes(data, "battery_life")
        self.assertEqual(result, 2.0)

    def test_nonexistent_field(self):
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},
            {"battery_life": 2.0}
        ]
        result = get_min_2_attributes(data, "non_existent_field")
        self.assertIsNone(result)

    def test_all_none_values(self):
        data = [
            {"price": None},
            {"price": None},
            {"price": None}
        ]
        result = get_min_2_attributes(data, "price")
        self.assertIsNone(result)

    def test_empty_list(self):
        data = []
        result = get_min_2_attributes(data, "price")
        self.assertIsNone(result)

    def test_mixed_numeric_types(self):
        data = [
            {"weight": 100},
            {"weight": 50.5},
            {"weight": 75}
        ]
        result = get_min_2_attributes(data, "weight")
        self.assertEqual(result, 50.5)

    def test_single_valid_value(self):
        data = [
            {"price": None},
            {"price": None},
            {"price": 99.99}
        ]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, 99.99)

    def test_negative_values(self):
        data = [
            {"temperature": -5.5},
            {"temperature": -10.2},
            {"temperature": -3.1}
        ]
        result = get_min_2_attributes(data, "temperature")
        self.assertEqual(result, -10.2)

    def test_zero_value(self):
        data = [
            {"stock": 0},
            {"stock": 5},
            {"stock": 10}
        ]
        result = get_min_2_attributes(data, "stock")
        self.assertEqual(result, 0)

    def test_large_numbers(self):
        data = [
            {"population": 1000000000},
            {"population": 500000000},
            {"population": 2000000000}
        ]
        result = get_min_2_attributes(data, "population")
        self.assertEqual(result, 500000000)

    def test_string_values_should_be_ignored(self):
        data = [
            {"name": "Alice"},
            {"name": "Bob"},
            {"name": "Charlie"}
        ]
        result = get_min_2_attributes(data, "name")
        self.assertIsNone(result)

    def test_mixed_valid_and_invalid_entries(self):
        data = [
            {"rating": 4.5},
            {"rating": None},
            {"rating": 3.2},
            {"other_field": "value"}
        ]
        result = get_min_2_attributes(data, "rating")
        self.assertEqual(result, 3.2)

    def test_rounding_to_two_decimals(self):
        data = [
            {"price": 10.123},
            {"price": 10.126},
            {"price": 10.124}
        ]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, 10.12)