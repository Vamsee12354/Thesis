import unittest
from implementation_manual import get_min_2_attributes

class TestGetMin2Attributes(unittest.TestCase):
    def test_happy_path_numeric_values(self):
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},
            {"battery_life": 2.0}
        ]
        self.assertEqual(get_min_2_attributes(data, "price"), 29.99)
        self.assertEqual(get_min_2_attributes(data, "battery_life"), 2.0)

    def test_non_existent_attribute(self):
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5}
        ]
        self.assertIsNone(get_min_2_attributes(data, "non_existent_field"))

    def test_all_values_none(self):
        data = [
            {"price": None, "battery_life": 4.0},
            {"price": None, "battery_life": 3.5}
        ]
        self.assertIsNone(get_min_2_attributes(data, "price"))

    def test_empty_list(self):
        self.assertIsNone(get_min_2_attributes([], "price"))

    def test_mixed_none_values(self):
        data = [
            {"price": 49.99},
            {"price": None},
            {"price": 29.99},
            {}
        ]
        self.assertEqual(get_min_2_attributes(data, "price"), 29.99)

    def test_non_numeric_values(self):
        data = [
            {"title": "A"},
            {"title": "B"},
            {"title": "C"}
        ]
        self.assertIsNone(get_min_2_attributes(data, "title"))

    def test_rounding_to_two_decimals(self):
        data = [
            {"price": 49.9999},
            {"price": 29.995},
            {"price": 29.994}
        ]
        self.assertEqual(get_min_2_attributes(data, "price"), 29.99)

    def test_integer_values(self):
        data = [
            {"quantity": 10},
            {"quantity": 5},
            {"quantity": 15}
        ]
        self.assertEqual(get_min_2_attributes(data, "quantity"), 5.0)

    def test_single_valid_value(self):
        data = [
            {"price": None},
            {"price": 49.99},
            {"price": None}
        ]
        self.assertEqual(get_min_2_attributes(data, "price"), 49.99)