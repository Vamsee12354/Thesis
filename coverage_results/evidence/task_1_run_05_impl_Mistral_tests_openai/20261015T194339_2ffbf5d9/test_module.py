import unittest
from implementation_manual import get_unique

class TestGetUniqueBrands(unittest.TestCase):

    def test_normal_case_with_valid_brands(self):
        # Arrange
        input_data = [{'brand': 'Brandname1'}, {'brand': 'Brandname2'}, {'brand': 'Brandname3'}]
        expected = ['Brandname1', 'Brandname2', 'Brandname3']
        # Act
        result = get_unique(input_data)
        # Assert
        self.assertEqual(result, expected)

    def test_empty_list_returns_none(self):
        # Arrange
        input_data = []
        # Act
        result = get_unique(input_data)
        # Assert
        self.assertIsNone(result)

    def test_all_invalid_brands_return_none(self):
        # Arrange
        input_data = [{'brand': None}, {'brand': ''}, {'brand': ' '}, {'brand': None}]
        # Act
        result = get_unique(input_data)
        # Assert
        self.assertIsNone(result)

    def test_mixed_duplicates_and_blanks(self):
        # Arrange
        input_data = [
            {'brand': 'Brandname'},
            {'brand': 'BrAnDNAme'},
            {'brand': 'BRANDNAME'},
            {'brand': 'brandname'},
            {'brand': None},
            {'brand': ' '}
        ]
        expected = ['Brandname']
        # Act
        result = get_unique(input_data)
        # Assert
        self.assertEqual(result, expected)

    def test_case_insensitivity_and_capitalization(self):
        # Arrange
        input_data = [
            {'brand': 'apple'},
            {'brand': 'Apple'},
            {'brand': 'APPLE'},
            {'brand': 'aPpLe'}
        ]
        expected = ['Apple']
        # Act
        result = get_unique(input_data)
        # Assert
        self.assertEqual(result, expected)

    def test_brands_with_leading_and_trailing_spaces(self):
        # Arrange
        input_data = [
            {'brand': '  Nike'},
            {'brand': 'nike  '},
            {'brand': '  NIKE  '}
        ]
        expected = ['Nike']
        # Act
        result = get_unique(input_data)
        # Assert
        self.assertEqual(result, expected)

    def test_multiple_valid_brands_with_duplicates_and_spaces(self):
        # Arrange
        input_data = [
            {'brand': 'Adidas'},
            {'brand': 'adidas'},
            {'brand': 'Puma'},
            {'brand': 'puma '},
            {'brand': 'Reebok'},
            {'brand': 'REEBOK'},
            {'brand': None},
            {'brand': ''}
        ]
        expected = ['Adidas', 'Puma', 'Reebok']
        # Act
        result = get_unique(input_data)
        # Assert
        self.assertEqual(result, expected)

    def test_brands_with_only_spaces_are_filtered_out(self):
        # Arrange
        input_data = [{'brand': '   '}, {'brand': '  '}, {'brand': '\t'}, {'brand': '\n'}]
        # Act
        result = get_unique(input_data)
        # Assert
        self.assertIsNone(result)

    def test_single_valid_brand(self):
        # Arrange
        input_data = [{'brand': 'Sony'}]
        expected = ['Sony']
        # Act
        result = get_unique(input_data)
        # Assert
        self.assertEqual(result, expected)

    def test_single_invalid_brand_none(self):
        # Arrange
        input_data = [{'brand': None}]
        # Act
        result = get_unique(input_data)
        # Assert
        self.assertIsNone(result)

    def test_single_invalid_brand_empty_string(self):
        # Arrange
        input_data = [{'brand': ''}]
        # Act
        result = get_unique(input_data)
        # Assert
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()