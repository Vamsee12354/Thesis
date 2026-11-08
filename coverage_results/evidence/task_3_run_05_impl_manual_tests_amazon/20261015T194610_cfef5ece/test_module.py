import unittest
from implementation_manual import get_min_2_attributes

class TestGetMin2Attributes(unittest.TestCase):

    def test_valid_attribute_with_values(self):
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
            {"price": 29.99, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},
            {"battery_life": 2.0}
        ]
        self.assertIsNone(get_min_2_attributes(data, "non_existent_field"))

    def test_all_values_none(self):
        data = [
            {"price": None, "battery_life": None},
            {"price": None, "battery_life": None}
        ]
        self.assertIsNone(get_min_2_attributes(data, "price"))
        self.assertIsNone(get_min_2_attributes(data, "battery_life"))

    def test_empty_data_list(self):
        data = []
        self.assertIsNone(get_min_2_attributes(data, "price"))
        self.assertIsNone(get_min_2_attributes(data, "battery_life"))

    def test_non_numeric_attribute(self):
        data = [
            {"title": "A"},
            {"title": "B"},
            {"title": "C"},
            {"title": "None"}
        ]
        self.assertIsNone(get_min_2_attributes(data, "title"))

if __name__ == '__main__':
    unittest.main()
