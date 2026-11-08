import unittest
from implementation_manual import get_average_price

class TestGetAveragePrice(unittest.TestCase):

    def test_valid_prices(self):
        price_list = [{'price': 100}, {'price': 200}, {'price': None}, {'price': 300}]
        self.assertEqual(get_average_price(price_list), 200.0)

    def test_all_missing_prices(self):
        price_list = [{'price': None}, {'price': None}]
        self.assertIsNone(get_average_price(price_list))

    def test_single_valid_price(self):
        price_list = [{'price': 150}, {'price': None}]
        self.assertEqual(get_average_price(price_list), 150.0)

    def test_empty_price_list(self):
        price_list = []
        self.assertIsNone(get_average_price(price_list))

    def test_no_valid_prices(self):
        price_list = [{'price': None}, {'price': None}, {'price': None}]
        self.assertIsNone(get_average_price(price_list))

if __name__ == '__main__':
    unittest.main()
