import unittest
from implementation_manual import get_min_2_attributes

class TestGetMin2Attributes(unittest.TestCase):
    def test_valid_price(self):
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},  
            {"battery_life": 2.0}                   
        ]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, 29.99)

    def test_valid_battery_life(self):
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

    def test_non_numeric_attribute(self):
        data = [
            {"title": "A"},
            {"title": "B"},
            {"title": "C"},  
            {"title": "None"}                   
        ]
        result = get_min_2_attributes(data, "title")
        self.assertIsNone(result)

    def test_mixed_numeric_and_non_numeric(self):
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": "twenty", "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},  
            {"battery_life": 2.0}                   
        ]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, 49.99)

    def test_rounded_to_two_decimals(self):
        data = [
            {"price": 49.999, "battery_life": 4.0},
            {"price": 29.995, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},  
            {"battery_life": 2.0}                   
        ]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, 30.0)

if __name__ == '__main__':
    unittest.main()