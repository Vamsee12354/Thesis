from implementation_manual import get_average_price
import unittest

class TestGetAveragePrice(unittest.TestCase):

    def test_normal_case_with_valid_prices(self):
        price_list = [{'price': 100}, {'price': 200}, {'price': None}, {'price': 300}]
        result = get_average_price(price_list)
        self.assertEqual(result, 200.0)

    def test_all_prices_none(self):
        price_list = [{'price': None}, {'price': None}]
        result = get_average_price(price_list)
        self.assertIsNone(result)

    def test_empty_price_list(self):
        price_list = []
        result = get_average_price(price_list)
        self.assertIsNone(result)

    def test_single_valid_price(self):
        price_list = [{'price': 50}]
        result = get_average_price(price_list)
        self.assertEqual(result, 50.0)

    def test_mixed_valid_and_none_prices(self):
        price_list = [{'price': 10}, {'price': None}, {'price': 20}, {'price': None}]
        result = get_average_price(price_list)
        self.assertEqual(result, 15.0)

    def test_prices_with_decimal_values(self):
        price_list = [{'price': 10.5}, {'price': 20.5}, {'price': None}]
        result = get_average_price(price_list)
        self.assertEqual(result, 15.5)

    def test_prices_with_zero(self):
        price_list = [{'price': 0}, {'price': 0}, {'price': None}]
        result = get_average_price(price_list)
        self.assertEqual(result, 0.0)

    def test_large_price_list(self):
        price_list = [{'price': i} for i in range(1, 1001)]
        result = get_average_price(price_list)
        self.assertEqual(result, 500.5)