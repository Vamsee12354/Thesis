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

    def test_all_products_missing_price(self):
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

    def test_single_product_with_price(self):
        # Arrange
        price_list = [{'price': 50.5}]
        expected_output = 50.5

        # Act
        result = get_average_price(price_list)

        # Assert
        self.assertEqual(result, expected_output)

    def test_single_product_without_price(self):
        # Arrange
        price_list = [{'price': None}]
        expected_output = None

        # Act
        result = get_average_price(price_list)

        # Assert
        self.assertIsNone(result)

    def test_rounding_to_two_decimals(self):
        # Arrange
        # (10 + 20 + 10) / 3 = 13.3333...
        price_list = [{'price': 10}, {'price': 20}, {'price': 10}]
        expected_output = 13.33

        # Act
        result = get_average_price(price_list)

        # Assert
        self.assertEqual(result, expected_output)

    def test_mixed_floats_and_integers(self):
        # Arrange
        price_list = [{'price': 10.5}, {'price': 20}, {'price': 30.75}]
        # (10.5 + 20 + 30.75) / 3 = 61.25 / 3 = 20.4166...
        expected_output = 20.42

        # Act
        result = get_average_price(price_list)

        # Assert
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()