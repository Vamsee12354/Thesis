import unittest
from implementation_manual import get_average_price

class TestGetAveragePrice(unittest.TestCase):

    def test_average_price_normal_case(self):
        # Arrange
        price_list = [{'price': 100}, {'price': 200}, {'price': None}, {'price': 300}]
        expected_output = 200.0

        # Act
        result = get_average_price(price_list)

        # Assert
        self.assertEqual(result, expected_output)

    def test_average_price_with_rounding(self):
        # Arrange
        price_list = [{'price': 10.555}, {'price': 20.111}]
        # (10.555 + 20.111) / 2 = 15.333 -> rounded to 15.33
        expected_output = 15.33

        # Act
        result = get_average_price(price_list)

        # Assert
        self.assertEqual(result, expected_output)

    def test_average_price_single_valid_product(self):
        # Arrange
        price_list = [{'price': 50.0}, {'price': None}]
        expected_output = 50.0

        # Act
        result = get_average_price(price_list)

        # Assert
        self.assertEqual(result, expected_output)

    def test_average_price_all_none(self):
        # Arrange
        price_list = [{'price': None}, {'price': None}]
        expected_output = None

        # Act
        result = get_average_price(price_list)

        # Assert
        self.assertIsNone(result)

    def test_average_price_empty_list(self):
        # Arrange
        price_list = []
        expected_output = None

        # Act
        result = get_average_price(price_list)

        # Assert
        self.assertIsNone(result)

    def test_average_price_mixed_types_and_none(self):
        # Arrange
        price_list = [{'price': 10}, {'price': None}, {'price': 20.5}]
        # (10 + 20.5) / 2 = 15.25
        expected_output = 15.25

        # Act
        result = get_average_price(price_list)

        # Assert
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()