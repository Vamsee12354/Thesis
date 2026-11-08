import unittest
from implementation_manual import get_average_price

class TestGetAveragePrice(unittest.TestCase):
    def test_normal_case(self):
        price_list = [{'price': 100}, {'price': 200}, {'price': None}, {'price': 300}]
        result = get_average_price(price_list)
        self.assertEqual(result, 200.0)

    def test_empty_list(self):
        price_list = []
        result = get_average_price(price_list)
        self.assertIsNone(result)

    def test_all_none_prices(self):
        price_list = [{'price': None}, {'price': None}]
        result = get_average_price(price_list)
        self.assertIsNone(result)

    def test_single_valid_price(self):
        price_list = [{'price': 150.5}]
        result = get_average_price(price_list)
        self.assertEqual(result, 150.5)

    def test_rounding_to_two_decimals(self):
        price_list = [{'price': 100.555}, {'price': 200.444}]
        result = get_average_price(price_list)
        self.assertEqual(result, 150.5)

    def test_mixed_valid_and_none_prices(self):
        price_list = [{'price': None}, {'price': 50}, {'price': 100}, {'price': None}]
        result = get_average_price(price_list)
        self.assertEqual(result, 75.0)