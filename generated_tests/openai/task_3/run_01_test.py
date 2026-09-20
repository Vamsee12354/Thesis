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
            {"size": 5.1234},
            {"size": 7},
            {"size": 5.126}
        ]
        attribute = "size"
        expected = 5.12  # minimum is 5.1234 rounded to 2 decimals

        # Action
        result = get_min_2_attributes(data, attribute)

        # Verify
        self.assertEqual(result, expected)

    def test_non_numeric_values_ignored(self):
        # Setup
        data = [
            {"rating": "high"},
            {"rating": None},
            {"rating": 4.5},
            {"rating": 3}
        ]
        attribute = "rating"
        expected = 3.00

        # Action
        result = get_min_2_attributes(data, attribute)

        # Verify
        self.assertEqual(result, expected)

    def test_all_values_non_numeric_or_none(self):
        # Setup
        data = [
            {"score": "low"},
            {"score": None},
            {"score": "medium"}
        ]
        attribute = "score"
        expected = None

        # Action
        result = get_min_2_attributes(data, attribute)

        # Verify
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()