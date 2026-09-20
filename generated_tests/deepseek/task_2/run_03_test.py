import unittest
from implementation_manual import get_average_price

class TestGetAveragePrice(unittest.TestCase):
    def test_normal_case(self):
        price_list = [{'price': 100}, {'price': 200}, {'price': None}, {'price': 300}]
        self.assertEqual(get_average_price(price_list), 200.0)

    def test_all_prices_none(self):
        price_list = [{'price': None}, {'price': None}]
        self.assertIsNone(get_average_price(price_list))

    def test_empty_list(self):
        price_list = []
        self.assertIsNone(get_average_price(price_list))

    def test_single_valid_price(self):
        price_list = [{'price': 150.5}]
        self.assertEqual(get_average_price(price_list), 150.5)

    def test_multiple_prices_with_decimals(self):
        price_list = [{'price': 10.25}, {'price': 20.75}, {'price': 30.50}]
        self.assertEqual(get_average_price(price_list), 20.5)

    def test_mixed_valid_and_none_prices(self):
        price_list = [{'price': None}, {'price': 50}, {'price': None}, {'price': 150}]
        self.assertEqual(get_average_price(price_list), 100.0)

    def test_all_prices_zero(self):
        price_list = [{'price': 0}, {'price': 0}, {'price': 0}]
        self.assertEqual(get_average_price(price_list), 0.0)