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

    def test_all_none_values(self):
        data = [
            {"price": None, "battery_life": 4.0},
            {"price": None, "battery_life": 3.5}
        ]
        self.assertIsNone(get_min_2_attributes(data, "price"))

    def test_empty_list(self):
        self.assertIsNone(get_min_2_attributes([], "price"))

    def test_mixed_none_and_values(self):
        data = [
            {"price": 100.0},
            {"price": None},
            {"price": 50.0},
            {"other_attr": 200.0}
        ]
        self.assertEqual(get_min_2_attributes(data, "price"), 50.0)

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
            {"price": 30.004}
        ]
        self.assertEqual(get_min_2_attributes(data, "price"), 30.0)

    def test_single_valid_value(self):
        data = [{"price": 99.99}]
        self.assertEqual(get_min_2_attributes(data, "price"), 99.99)

    def test_single_invalid_value(self):
        data = [{"price": None}]
        self.assertIsNone(get_min_2_attributes(data, "price"))