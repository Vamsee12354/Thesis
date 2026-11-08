import unittest
from implementation_manual import get_average_price

class TestGetAveragePrice(unittest.TestCase):

    def test_normal_case_with_valid_prices(self):
        # Arrange
        price_list = [{'price': 100}, {'price': 200}, {'price': None}, {'price': 300}]
        expected_output = 200.0

        # Act
        result = get_average_price(price_list)

        # Assert
        self.assertEqual(result, expected_output)

    def test_single_valid_price(self):
        # Arrange
        price_list = [{'price': 50.555}, {'price': None}]
        expected_output = 50.56

        # Act
        result = get_average_price(price_list)

        # Assert
        self.assertEqual(result, expected_output)

    def test_all_prices_are_none(self):
        # Arrange
        price_list = [{'price': None}, {'price': None}]
        expected_output = None

        # Act
        result = get_average_price(price_list)

        # Assert
        self.assertIsNone(result)

    def test_empty_list(self):
        # Arrange
        price_list = []
        expected_output = None

        # Act
        result = get_average_price(price_list)

        # Assert
        self.assertIsNone(result)

    def test_rounding_to_two_decimals(self):
        # Arrange
        # (10.11 + 20.22 + 30.33) / 3 = 60.66 / 3 = 20.22
        # Using values that require specific rounding
        price_list = [{'price': 10.111}, {'price': 20.222}, {'price': 30.333}]
        expected_output = 20.22

        # Act
        result = get_average_price(price_list)

        # Assert
        self.assertEqual(result, expected_output)

    def test_mixed_types_and_none(self):
        # Arrange
        price_list = [{'price': 10}, {'price': 20}, {'price': None}, {'price': 30}]
        expected_output = 20.0

        # Act
        result = get_average_price(price_list)

        # Assert
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()