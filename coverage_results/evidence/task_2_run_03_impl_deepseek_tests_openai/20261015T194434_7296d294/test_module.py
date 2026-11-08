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

    def test_prices_with_zero_and_none(self):
        # Setup
        price_list = [{'price': 0}, {'price': None}, {'price': 100}]
        # Action
        result = get_average_price(price_list)
        # Verify
        self.assertEqual(result, 50.0)

    def test_prices_with_floats_and_rounding(self):
        # Setup
        price_list = [{'price': 10.123}, {'price': 20.456}, {'price': None}]
        # Action
        result = get_average_price(price_list)
        # Verify
        self.assertEqual(result, round((10.123 + 20.456) / 2, 2))

    def test_prices_all_none_and_empty_dicts(self):
        # Setup
        price_list = [{'price': None}, {}, {'price': None}]
        # Action
        result = get_average_price(price_list)
        # Verify
        self.assertIsNone(result)

    def test_prices_with_missing_price_key(self):
        # Setup
        price_list = [{'price': 100}, {'cost': 200}, {'price': 300}]
        # Action
        result = get_average_price(price_list)
        # Verify
        self.assertEqual(result, 200.0)

    def test_prices_with_non_numeric_price(self):
        # Setup
        price_list = [{'price': 100}, {'price': '200'}, {'price': 300}]
        # Action & Verify
        with self.assertRaises(TypeError):
            get_average_price(price_list)

if __name__ == '__main__':
    unittest.main()