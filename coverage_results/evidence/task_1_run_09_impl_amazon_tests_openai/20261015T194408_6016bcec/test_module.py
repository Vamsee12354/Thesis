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

    def test_all_invalid_brands_none_or_empty(self):
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
            {'brand': 'APPLE'},
            {'brand': 'Apple'},
            {'brand': 'aPpLe'}
        ]
        expected = ['Apple']
        # Act
        result = get_unique(input_data)
        # Assert
        self.assertEqual(result, expected)

    def test_multiple_brands_with_mixed_cases_and_spaces(self):
        # Arrange
        input_data = [
            {'brand': '  nike '},
            {'brand': 'NIKE'},
            {'brand': 'Adidas'},
            {'brand': 'adidas '},
            {'brand': 'Puma'},
            {'brand': 'puma'},
            {'brand': ' '},
            {'brand': None}
        ]
        expected = ['Nike', 'Adidas', 'Puma']
        # Act
        result = get_unique(input_data)
        # Assert
        self.assertEqual(result, expected)

    def test_brands_with_only_spaces_are_filtered_out(self):
        # Arrange
        input_data = [{'brand': '   '}, {'brand': '  '}, {'brand': None}]
        # Act
        result = get_unique(input_data)
        # Assert
        self.assertIsNone(result)

    def test_brands_with_non_string_values_ignored(self):
        # Arrange
        input_data = [{'brand': 'ValidBrand'}, {'brand': 123}, {'brand': None}, {'brand': ''}]
        expected = ['Validbrand']
        # Act
        result = get_unique(input_data)
        # Assert
        self.assertEqual(result, expected)

    def test_order_preserved_in_output(self):
        # Arrange
        input_data = [
            {'brand': 'firstBrand'},
            {'brand': 'SecondBrand'},
            {'brand': 'firstbrand'},
            {'brand': 'thirdBrand'},
            {'brand': 'secondbrand'}
        ]
        expected = ['Firstbrand', 'Secondbrand', 'Thirdbrand']
        # Act
        result = get_unique(input_data)
        # Assert
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()