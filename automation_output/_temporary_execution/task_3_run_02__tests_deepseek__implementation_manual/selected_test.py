import unittest
from implementation_manual import get_min_2_attributes

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

    def test_non_existent_field(self):
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

    def test_non_numeric_values(self):
        data = [
            {"title": "A"},
            {"title": "B"},
            {"title": "C"},  
            {"title": "None"}                   
        ]
        result = get_min_2_attributes(data, "title")
        self.assertIsNone(result)

    def test_rounding_to_two_decimals(self):
        data = [
            {"price": 49.999, "battery_life": 4.0},
            {"price": 29.991, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},  
            {"battery_life": 2.0}                   
        ]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, 29.99)

    def test_mixed_numeric_and_none(self):
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": None, "battery_life": 3.5},
            {"price": 10.0, "battery_life": 5.0},  
            {"price": 5.55, "battery_life": 2.0}                   
        ]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, 5.55)