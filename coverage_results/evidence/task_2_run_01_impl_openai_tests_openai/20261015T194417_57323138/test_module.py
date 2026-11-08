import unittest
from implementation_manual import get_average_price

class TestGetAveragePrice(unittest.TestCase):

    def test_average_with_valid_prices(self):
        # Setup
        price_list = [{'price': 100}, {'price': 200}, {'price': None}, {'price': 300}]
        # Action
        result = get_average_price(price_list)
        # Verify
        self.assertEqual(result, 200.0)

    def test_all_prices_none(self):
        # Setup
        price_list = [{'price': None}, {'price': None}]
        # Action
        result = get_average_price(price_list)
        # Verify
        self.assertIsNone(result)

    def test_empty_price_list(self):
        # Setup
        price_list = []
        # Action
        result = get_average_price(price_list)
        # Verify
        self.assertIsNone(result)

    def test_single_valid_price(self):
        # Setup
        price_list = [{'price': None}, {'price': 150}, {'price': None}]
        # Action
        result = get_average_price(price_list)
        # Verify
        self.assertEqual(result, 150.0)

    def test_prices_with_floats_and_rounding(self):
        # Setup
        price_list = [{'price': 100.123}, {'price': 200.456}, {'price': 300.789}]
        # Action
        result = get_average_price(price_list)
        # Verify
        expected_average = round((100.123 + 200.456 + 300.789) / 3, 2)
        self.assertEqual(result, expected_average)

    def test_prices_with_zero_and_none(self):
        # Setup
        price_list = [{'price': 0}, {'price': None}, {'price': 50}]
        # Action
        result = get_average_price(price_list)
        # Verify
        expected_average = round((0 + 50) / 2, 2)
        self.assertEqual(result, expected_average)

    def test_prices_all_zero(self):
        # Setup
        price_list = [{'price': 0}, {'price': 0}, {'price': 0}]
        # Action
        result = get_average_price(price_list)
        # Verify
        self.assertEqual(result, 0.0)

    def test_prices_with_non_numeric_values_ignored(self):
        # Setup
        price_list = [{'price': 100}, {'price': 'invalid'}, {'price': None}, {'price': 200}]
        # Action
        result = get_average_price(price_list)
        # Verify
        # Assuming non-numeric values are ignored or cause no error, only 100 and 200 counted
        self.assertEqual(result, 150.0)

if __name__ == '__main__':
    unittest.main()