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

    def test_mixed_valid_and_none_prices(self):
        price_list = [{'price': 50}, {'price': None}, {'price': 75}, {'price': None}]
        self.assertEqual(get_average_price(price_list), 62.5)

    def test_rounding_to_two_decimals(self):
        price_list = [{'price': 33.333}, {'price': 66.666}]
        self.assertEqual(get_average_price(price_list), 50.0)

    def test_all_prices_zero(self):
        price_list = [{'price': 0}, {'price': 0}]
        self.assertEqual(get_average_price(price_list), 0.0)