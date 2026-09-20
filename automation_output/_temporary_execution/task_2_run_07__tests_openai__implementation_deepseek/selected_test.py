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

    def test_prices_with_floats(self):
        # Setup
        price_list = [{'price': 10.555}, {'price': 20.445}]
        # Action
        result = get_average_price(price_list)
        # Verify
        self.assertEqual(result, 15.5)

    def test_prices_with_negative_and_positive(self):
        # Setup
        price_list = [{'price': -10}, {'price': 20}]
        # Action
        result = get_average_price(price_list)
        # Verify
        self.assertEqual(result, 5.0)

    def test_prices_with_all_none_and_empty_dicts(self):
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

if __name__ == '__main__':
    unittest.main()