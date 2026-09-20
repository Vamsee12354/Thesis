from implementation_manual import get_min_2_attributes
import unittest

class TestGetMin2Attributes(unittest.TestCase):

    def test_happy_path_price_attribute(self):
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},
            {"battery_life": 2.0}
        ]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, 29.99)

    def test_happy_path_battery_life_attribute(self):
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},
            {"battery_life": 2.0}
        ]
        result = get_min_2_attributes(data, "battery_life")
        self.assertEqual(result, 2.0)

    def test_non_existent_field_returns_none(self):
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},
            {"battery_life": 2.0}
        ]
        result = get_min_2_attributes(data, "non_existent_field")
        self.assertIsNone(result)

    def test_all_none_values_returns_none(self):
        data = [
            {"price": None},
            {"price": None},
            {"price": None}
        ]
        result = get_min_2_attributes(data, "price")
        self.assertIsNone(result)

    def test_empty_list_returns_none(self):
        data = []
        result = get_min_2_attributes(data, "price")
        self.assertIsNone(result)

    def test_mixed_numeric_types_returns_min_float(self):
        data = [
            {"price": 50},
            {"price": 30.5},
            {"price": 40.25}
        ]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, 30.5)

    def test_single_valid_value_returns_that_value(self):
        data = [
            {"price": None},
            {"price": None},
            {"price": 10.5}
        ]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, 10.5)

    def test_negative_values_returns_min(self):
        data = [
            {"price": -10.5},
            {"price": -20.0},
            {"price": -5.25}
        ]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, -20.0)

    def test_large_numbers_returns_min(self):
        data = [
            {"price": 1000000.123},
            {"price": 999999.999},
            {"price": 1000001.0}
        ]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, 999999.999)

    def test_rounding_to_two_decimals(self):
        data = [
            {"price": 10.126},
            {"price": 10.124},
            {"price": 10.125}
        ]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, 10.12)