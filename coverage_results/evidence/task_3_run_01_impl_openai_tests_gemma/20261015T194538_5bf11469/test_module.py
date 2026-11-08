import unittest
from implementation_manual import get_min_2_attributes

class TestGetMin2Attributes(unittest.TestCase):

    def test_happy_path_price(self):
        # Setup
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},
            {"battery_life": 2.0}
        ]
        dict_search = "price"
        
        # Action
        result = get_min_2_attributes(data, dict_search)
        
        # Verification
        self.assertEqual(result, 29.99)

    def test_happy_path_battery_life(self):
        # Setup
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},
            {"battery_life": 2.0}
        ]
        dict_search = "battery_life"
        
        # Action
        result = get_min_2_attributes(data, dict_search)
        
        # Verification
        self.assertEqual(result, 2.0)

    def test_rounding_to_two_decimals(self):
        # Setup
        data = [
            {"val": 10.555},
            {"val": 10.554},
            {"val": 10.556}
        ]
        dict_search = "val"
        
        # Action
        result = get_min_2_attributes(data, dict_search)
        
        # Verification
        self.assertEqual(result, 10.55)

    def test_non_existent_field(self):
        # Setup
        data = [
            {"price": 49.99},
            {"battery_life": 3.5}
        ]
        dict_search = "non_existent_field"
        
        # Action
        result = get_min_2_attributes(data, dict_search)
        
        # Verification
        self.assertIsNone(result)

    def test_all_values_are_none(self):
        # Setup
        data = [
            {"price": None},
            {"price": None},
            {"other": 10}
        ]
        dict_search = "price"
        
        # Action
        result = get_min_2_attributes(data, dict_search)
        
        # Verification
        self.assertIsNone(result)

    def test_empty_list(self):
        # Setup
        data = []
        dict_search = "price"
        
        # Action
        result = get_min_2_attributes(data, dict_search)
        
        # Verification
        self.assertIsNone(result)

    def test_non_numeric_values(self):
        # Setup
        data = [
            {"title": "A"},
            {"title": "B"},
            {"title": None}
        ]
        dict_search = "title"
        
        # Action
        result = get_min_2_attributes(data, dict_search)
        
        # Verification
        self.assertIsNone(result)

    def test_mixed_numeric_types(self):
        # Setup
        data = [
            {"val": 10},
            {"val": 5.5},
            {"val": 15.75}
        ]
        dict_search = "val"
        
        # Action
        result = get_min_2_attributes(data, dict_search)
        
        # Verification
        self.assertEqual(result, 5.5)

if __name__ == '__main__':
    unittest.main()