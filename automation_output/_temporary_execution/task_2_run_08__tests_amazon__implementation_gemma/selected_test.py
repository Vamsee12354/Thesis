import unittest
from implementation_manual import get_average_price

class TestGetAveragePrice(unittest.TestCase):

    def test_normal_case_with_valid_prices(self):
        price_list = [{'price': 100}, {'price': 200}, {'price': None}, {'price': 300}]
        self.assertEqual(get_average_price(price_list), 200.0)

    def test_all_products_missing_price(self):
        price_list = [{'price': None}, {'price': None}]
        self.assertIsNone(get_average_price(price_list))

    def test_no_products(self):
        price_list = []
        self.assertIsNone(get_average_price(price_list))

    def test_single_product_with_price(self):
        price_list = [{'price': 150}]
        self.assertEqual(get_average_price(price_list), 150.0)

    def test_single_product_missing_price(self):
        price_list = [{'price': None}]
        self.assertIsNone(get_average_price(price_list))

if __name__ == '__main__':
    unittest.main()
