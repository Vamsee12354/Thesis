import unittest
from implementation_manual import get_unique

class TestGetUniqueBrands(unittest.TestCase):

    def test_normal_case_with_valid_brands(self):
        # Arrange
        input_data = [
            {'brand': 'Brandname1'},
            {'brand': 'Brandname2'},
            {'brand': 'Brandname3'}
        ]
        expected = ['Brandname1', 'Brandname2', 'Brandname3']

        # Act
        result = get_unique(input_data)

        # Assert
        self.assertEqual(result, expected)

    def test_empty_list_returns_none(self):
        # Arrange
        input_data = []
        expected = None

        # Act
        result = get_unique(input_data)

        # Assert
        self.assertIsNone(result)

    def test_all_invalid_or_missing_brands_return_none(self):
        # Arrange
        input_data = [
            {'brand': None},
            {'brand': ''},
            {'brand': ' '},
            {'brand': None}
        ]
        expected = None

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
            {'brand': 'APPLE'},
            {'brand': 'Apple'},
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

    def test_multiple_unique_brands_with_varied_cases_and_spaces(self):
        # Arrange
        input_data = [
            {'brand': '  Samsung'},
            {'brand': 'samsung  '},
            {'brand': 'Apple'},
            {'brand': 'apple'},
            {'brand': '  LG'},
            {'brand': 'lg'},
            {'brand': None},
            {'brand': ''}
        ]
        expected = ['Samsung', 'Apple', 'Lg']

        # Act
        result = get_unique(input_data)

        # Assert
        self.assertEqual(result, expected)

    def test_brands_with_non_string_values_ignored(self):
        # Arrange
        input_data = [
            {'brand': 'Sony'},
            {'brand': 123},
            {'brand': None},
            {'brand': ' '},
            {'brand': 'sony'}
        ]
        expected = ['Sony']

        # Act
        result = get_unique(input_data)

        # Assert
        self.assertEqual(result, expected)

    def test_single_valid_brand(self):
        # Arrange
        input_data = [{'brand': 'UniqueBrand'}]
        expected = ['UniqueBrand']

        # Act
        result = get_unique(input_data)

        # Assert
        self.assertEqual(result, expected)

    def test_single_invalid_brand_none(self):
        # Arrange
        input_data = [{'brand': None}]
        expected = None

        # Act
        result = get_unique(input_data)

        # Assert
        self.assertIsNone(result)

    def test_single_invalid_brand_empty_string(self):
        # Arrange
        input_data = [{'brand': ''}]
        expected = None

        # Act
        result = get_unique(input_data)

        # Assert
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()