import unittest
from implementation_manual import get_average_price

class TestGetAveragePrice(unittest.TestCase):

    def test_normal_case_with_valid_prices(self):
        # Setup
        price_list = [{'price': 100}, {'price': 200}, {'price': None}, {'price': 300}]
        expected_output = 200.0

        # Action
        result = get_average_price(price_list)

        # Verification
        self.assertEqual(result, expected_output)

    def test_single_valid_price(self):
        # Setup
        price_list = [{'price': 50.555}, {'price': None}]
        expected_output = 50.56

        # Action
        result = get_average_price(price_list)

        # Verification
        self.assertEqual(result, expected_output)

    def test_all_prices_are_none(self):
        # Setup
        price_list = [{'price': None}, {'price': None}]
        
        # Action
        result = get_average_price(price_list)

        # Verification
        self.assertIsNone(result)

    def test_empty_list(self):
        # Setup
        price_list = []
        
        # Action
        result = get_average_price(price_list)

        # Verification
        self.assertIsNone(result)

    def test_rounding_to_two_decimals(self):
        # Setup
        # (10.11 + 10.12 + 10.14) / 3 = 30.37 / 3 = 10.12333...
        price_list = [{'price': 10.11}, {'price': 10.12}, {'price': 10.14}]
        expected_output = 10.12

        # Action
        result = get_average_price(price_list)

        # Verification
        self.assertEqual(result, expected_output)

    def test_mixed_types_and_none(self):
        # Setup
        price_list = [{'price': 10}, {'price': None}, {'price': 20.5}]
        expected_output = 15.25

        # Action
        result = get_average_price(price_list)

        # Verification
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()