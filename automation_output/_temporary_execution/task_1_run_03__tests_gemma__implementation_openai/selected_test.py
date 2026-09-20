import unittest
from implementation_manual import get_unique

class TestGetUnique(unittest.TestCase):

    def test_get_unique_normal_case(self):
        # Arrange
        brands = [{'brand': 'Brandname1'}, {'brand': 'Brandname2'}, {'brand': 'Brandname3'}]
        expected = ['Brandname1', 'Brandname2', 'Brandname3']

        # Act
        result = get_unique(*brands)

        # Assert
        self.assertEqual(result, expected)

    def test_get_unique_empty_input(self):
        # Arrange
        brands = []
        expected = None

        # Act
        result = get_unique(*brands)

        # Assert
        self.assertIsNone(result)

    def test_get_unique_all_invalid_values(self):
        # Arrange
        brands = [{'brand': None}, {'brand': ''}, {'brand': ' '}]
        expected = None

        # Act
        result = get_unique(*brands)

        # Assert
        self.assertIsNone(result)

    def test_get_unique_case_insensitivity_and_normalization(self):
        # Arrange
        brands = [
            {'brand': 'Brandname'}, 
            {'brand': 'BrAnDNAme'}, 
            {'brand': 'BRANDNAME'}, 
            {'brand': 'brandname'},
            {'brand': None}, 
            {'brand': ' '}
        ]
        expected = ['Brandname']

        # Act
        result = get_unique(*brands)

        # Assert
        self.assertEqual(result, expected)

    def test_get_unique_whitespace_handling(self):
        # Arrange
        brands = [{'brand': '  Apple  '}, {'brand': 'Apple'}]
        expected = ['Apple']

        # Act
        result = get_unique(*brands)

        # Assert
        self.assertEqual(result, expected)

    def test_get_unique_preserves_order_of_first_appearance(self):
        # Arrange
        # The spec says "Do not sort the final output list"
        # We test that it maintains the order of the first valid occurrence
        brands = [
            {'brand': 'Zebra'}, 
            {'brand': 'Apple'}, 
            {'brand': 'zebra'}, 
            {'brand': 'Apple'}
        ]
        expected = ['Zebra', 'Apple']

        # Act
        result = get_unique(*brands)

        # Assert
        self.assertEqual(result, expected)

    def test_get_unique_mixed_valid_and_invalid(self):
        # Arrange
        brands = [
            {'brand': 'Nike'},
            {'brand': None},
            {'brand': 'Adidas'},
            {'brand': ''},
            {'brand': 'NIKE'}
        ]
        expected = ['Nike', 'Adidas']

        # Act
        result = get_unique(*brands)

        # Assert
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()