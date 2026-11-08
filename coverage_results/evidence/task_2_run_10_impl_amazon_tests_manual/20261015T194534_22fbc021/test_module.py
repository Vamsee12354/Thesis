# Tests for task2_get_average_price
import unittest
from implementation_manual import get_average_price


class Test_get_average_price(unittest.TestCase):
    def test_list_is_empty(self):
        self.assertIsNone(get_average_price([]))

    def test_working_list_price(self):
        prices=[{'price':1.5},{'price':2},{'price':4},{'price':0},{'price':-3},{'price':3},{'price':5}]
        self.assertAlmostEqual(get_average_price(prices),1.79)

    def test_highvalue_numbers(self):
        prices=[{'price':2313213123},{'price':1021232122.5323},{'price':20311111.76},{'price':101112321.21}]
        self.assertAlmostEqual(get_average_price(prices),863967169.63)

    def test_zero_value(self):
        self.assertEqual(get_average_price([{'price':0},{'price':0}]),0)

    def test_null_value(self):
        prices=[{'price':12},{'price':1232},{'price':None}, {'price':132}]
        self.assertEqual(get_average_price(prices),458.67)

    def test_multiple_nulls(self):
        self.assertIsNone(get_average_price([{'price':None}, {'price':None}]))

    def test_wrong_key(self):
        prices=[{'price123':12122},{'price1221':1211},{'price22':211},{'price155':98}]
        self.assertIsNone(get_average_price(prices))

    def test_no_products(self):
        prices=[{}]
        self.assertIsNone(get_average_price(prices))
        
    def test_numbers_inwords(self):
        prices=[{'price':'Twelve'}, {'price':'One Thousand and Thirty Two'}, {'price':None}, {'price':'One hundred and thirty two'}]
        self.assertIsNone(get_average_price(prices))
    

if __name__ == "__main__":
    unittest.main()
