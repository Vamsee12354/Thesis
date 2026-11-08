import unittest
from implementation_manual import get_min_2_attributes

class TestGetMin2Attributes(unittest.TestCase):

    def test_minimum_price_with_valid_data(self):
        # Setup
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},
            {"battery_life": 2.0}
        ]
        attribute = "price"
        expected = 29.99

        # Action
        result = get_min_2_attributes(data, attribute)

        # Verify
        self.assertEqual(result, expected)

    def test_minimum_battery_life_with_valid_data(self):
        # Setup
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},
            {"battery_life": 2.0}
        ]
        attribute = "battery_life"
        expected = 2.0

        # Action
        result = get_min_2_attributes(data, attribute)

        # Verify
        self.assertEqual(result, expected)

    def test_attribute_not_present_in_any_product(self):
        # Setup
        data = [
            {"price": 49.99, "battery_life": 4.0},
            {"price": 29.99, "battery_life": 3.5},
            {"price": None, "battery_life": 5.0},
            {"battery_life": 2.0}
        ]
        attribute = "non_existent_field"
        expected = None

        # Action
        result = get_min_2_attributes(data, attribute)

        # Verify
        self.assertIsNone(result)

    def test_all_values_none_for_attribute(self):
        # Setup
        data = [
            {"title": "A"},
            {"title": "B"},
            {"title": "C"},
            {"title": None}
        ]
        attribute = "title"
        expected = None

        # Action
        result = get_min_2_attributes(data, attribute)

        # Verify
        self.assertIsNone(result)

    def test_empty_data_list(self):
        # Setup
        data = []
        attribute = "price"
        expected = None

        # Action
        result = get_min_2_attributes(data, attribute)

        # Verify
        self.assertIsNone(result)

    def test_mixed_none_and_numeric_values(self):
        # Setup
        data = [
            {"weight": None},
            {"weight": 10},
            {"weight": 5.555},
            {"weight": None},
            {"weight": 7}
        ]
        attribute = "weight"
        expected = 5.56  # rounded to 2 decimals

        # Action
        result = get_min_2_attributes(data, attribute)

        # Verify
        self.assertEqual(result, expected)

    def test_integer_and_float_values(self):
        # Setup
        data = [
            {"size": 10},
            {"size": 3.14159},
            {"size": 7},
            {"size": 3.14}
        ]
        attribute = "size"
        expected = 3.14  # minimum rounded to 2 decimals

        # Action
        result = get_min_2_attributes(data, attribute)

        # Verify
        self.assertEqual(result, expected)

    def test_ignore_products_without_attribute(self):
        # Setup
        data = [
            {"price": 20},
            {"weight": 5},
            {"price": 15},
            {"weight": 10}
        ]
        attribute = "price"
        expected = 15.0

        # Action
        result = get_min_2_attributes(data, attribute)

        # Verify
        self.assertEqual(result, expected)

    def test_attribute_values_are_zero(self):
        # Setup
        data = [
            {"price": 0},
            {"price": 0.0},
            {"price": None},
            {"price": 5}
        ]
        attribute = "price"
        expected = 0.0

        # Action
        result = get_min_2_attributes(data, attribute)

        # Verify
        self.assertEqual(result, expected)

    def test_attribute_values_all_none_and_missing(self):
        # Setup
        data = [
            {"price": None},
            {"weight": 10},
            {"price": None},
            {"weight": 5}
        ]
        attribute = "price"
        expected = None

        # Action
        result = get_min_2_attributes(data, attribute)

        # Verify
        self.assertIsNone(result)