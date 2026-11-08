from implementation_manual import get_min_2_attributes
import unittest

class TestGetMin2Attributes(unittest.TestCase):

    def test_valid_numeric_attribute_with_mixed_values(self):
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},
            {"battery_life": 2.0}
        ]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, 29.99)

    def test_valid_numeric_attribute_with_all_values(self):
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5},
            {"price": 15.50, "battery_life": 5.0}
        ]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, 15.50)

    def test_valid_numeric_attribute_with_none_values(self):
        data = [
            {"price": None, "battery_life": 4.0},
            {"price": None, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0}
        ]
        result = get_min_2_attributes(data, "price")
        self.assertIsNone(result)

    def test_valid_numeric_attribute_with_empty_list(self):
        data = []
        result = get_min_2_attributes(data, "price")
        self.assertIsNone(result)

    def test_valid_numeric_attribute_with_single_product(self):
        data = [{"price": 10.50}]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, 10.50)

    def test_valid_numeric_attribute_with_negative_values(self):
        data = [
            {"price": -10.50},
            {"price": -20.75},
            {"price": -5.25}
        ]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, -20.75)

    def test_valid_numeric_attribute_with_integer_values(self):
        data = [
            {"price": 10},
            {"price": 20},
            {"price": 5}
        ]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, 5)

    def test_valid_numeric_attribute_with_float_values(self):
        data = [
            {"price": 10.5},
            {"price": 20.75},
            {"price": 5.25}
        ]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, 5.25)

    def test_non_existent_attribute(self):
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5}
        ]
        result = get_min_2_attributes(data, "non_existent_field")
        self.assertIsNone(result)

    def test_attribute_with_all_none_values(self):
        data = [
            {"price": None},
            {"price": None},
            {"price": None}
        ]
        result = get_min_2_attributes(data, "price")
        self.assertIsNone(result)

    def test_attribute_with_mixed_none_and_valid_values(self):
        data = [
            {"price": None},
            {"price": 10.5},
            {"price": None},
            {"price": 5.25}
        ]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, 5.25)

    def test_rounded_output_to_two_decimals(self):
        data = [
            {"price": 10.123},
            {"price": 5.456},
            {"price": 7.789}
        ]
        result = get_min_2_attributes(data, "price")
        self.assertEqual(result, 5.46)

    def test_attribute_with_string_values_raises_error(self):
        data = [
            {"title": "A"},
            {"title": "B"},
            {"title": "C"}
        ]
        with self.assertRaises(TypeError):
            get_min_2_attributes(data, "title")

    def test_attribute_with_mixed_types_including_none(self):
        data = [
            {"price": 10.5},
            {"price": "20.75"},
            {"price": None},
            {"price": 5.25}
        ]
        with self.assertRaises(TypeError):
            get_min_2_attributes(data, "price")