import unittest
from implementation_manual import get_min_2_attributes

class TestGetMin2Attributes(unittest.TestCase):
    def test_happy_path_single_attribute(self):
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},
            {"battery_life": 2.0}
        ]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, 29.99)

    def test_happy_path_another_attribute(self):
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},
            {"battery_life": 2.0}
        ]
        result = get_min_2_attributes(data, "battery_life")
        self.assertEqual(result, 2.0)

    def test_non_existent_attribute(self):
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
            {"price": None, "battery_life": 4.0},
            {"price": None, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},
            {"battery_life": 2.0}
        ]
        result = get_min_2_attributes(data, "price")
        self.assertIsNone(result)

    def test_empty_list(self):
        data = []
        result = get_min_2_attributes(data, "price")
        self.assertIsNone(result)

    def test_non_numeric_attribute(self):
        data = [
            {"title": "A"},
            {"title": "B"},
            {"title": "C"},
            {"title": "None"}
        ]
        result = get_min_2_attributes(data, "title")
        self.assertIsNone(result)

    def test_mixed_numeric_and_none(self):
        data = [
            {"price": 10.5, "battery_life": 4.0},
            {"price": None, "battery_life": 3.5},
            {"price": 5.99, "battery_life": 5.0},
            {"price": 7.25, "battery_life": None}
        ]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, 5.99)

    def test_single_valid_item(self):
        data = [{"price": 15.99}]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, 15.99)

    def test_rounding_to_two_decimals(self):
        data = [
            {"price": 10.555, "battery_life": 4.0},
            {"price": 10.554, "battery_life": 3.5},
            {"price": 10.556, "battery_life": 5.0}
        ]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, 10.55)

    def test_integer_values(self):
        data = [
            {"quantity": 10},
            {"quantity": 5},
            {"quantity": 15}
        ]
        result = get_min_2_attributes(data, "quantity")
        self.assertEqual(result, 5.0)