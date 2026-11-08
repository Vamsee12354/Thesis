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

    def test_mixed_prices_with_none(self):
        price_list = [{'price': 10}, {'price': None}, {'price': 30}, {'price': None}]
        result = get_average_price(price_list)
        self.assertEqual(result, 20.0)

    def test_all_prices_zero(self):
        price_list = [{'price': 0}, {'price': 0}, {'price': 0}]
        result = get_average_price(price_list)
        self.assertEqual(result, 0.0)

    def test_large_numbers(self):
        price_list = [{'price': 1000000}, {'price': 2000000}, {'price': 3000000}]
        result = get_average_price(price_list)
        self.assertEqual(result, 2000000.0)

    def test_negative_prices(self):
        price_list = [{'price': -100}, {'price': -200}, {'price': -300}]
        result = get_average_price(price_list)
        self.assertEqual(result, -200.0)

    def test_float_prices(self):
        price_list = [{'price': 10.5}, {'price': 20.5}, {'price': 30.5}]
        result = get_average_price(price_list)
        self.assertEqual(result, 20.5)

    def test_rounding_to_two_decimals(self):
        price_list = [{'price': 10.123}, {'price': 20.456}, {'price': 30.789}]
        result = get_average_price(price_list)
        self.assertEqual(result, 20.45)