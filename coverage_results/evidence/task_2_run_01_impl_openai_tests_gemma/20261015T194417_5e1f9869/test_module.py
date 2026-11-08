import unittest
from implementation_manual import get_average_price

class TestGetAveragePrice(unittest.TestCase):

    def test_average_calculation_with_valid_prices(self):
        # Arrange
        price_list = [{'price': 100}, {'price': 200}, {'price': None}, {'price': 300}]
        expected_output = 200.0

        # Act
        result = get_average_price(price_list)

        # Assert
        self.assertEqual(result, expected_output)

    def test_average_calculation_with_rounding(self):
        # Arrange
        price_list = [{'price': 10}, {'price': 20}, {'price': 15}]
        # (10 + 20 + 15) / 3 = 15.0
        expected_output = 15.0
        
        price_list_complex = [{'price': 10.555}, {'price': 20.123}]
        # (10.555 + 20.123) / 2 = 15.339 -> rounded to 15.34
        expected_output_complex = 15.34

        # Act
        result_simple = get_average_price(price_list)
        result_complex = get_average_price(price_list_complex)

        # Assert
        self.assertEqual(result_simple, expected_output)
        self.assertEqual(result_complex, expected_output_complex)

    def test_single_valid_price(self):
        # Arrange
        price_list = [{'price': None}, {'price': 50.0}, {'price': None}]
        expected_output = 50.0

        # Act
        result = get_average_price(price_list)

        # Assert
        self.assertEqual(result, expected_output)
        self.assertIsInstance(result, float)

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

    def test_list_with_empty_dictionary_values(self):
        # Arrange
        # Based on specification "Only products with non empty values : price are considered"
        # If price is missing from dict or is None
        price_list = [{'price': None}, {}]
        expected_output = None

        # Act
        result = get_average_price(price_list)

        # Assert
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()