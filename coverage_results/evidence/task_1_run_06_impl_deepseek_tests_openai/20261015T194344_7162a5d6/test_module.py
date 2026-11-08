import unittest
from implementation_manual import get_unique

class TestGetUniqueBrands(unittest.TestCase):

    def test_normal_case_with_valid_brands(self):
        # Setup
        input_data = [{'brand': 'Brandname1'}, {'brand': 'Brandname2'}, {'brand': 'Brandname3'}]
        expected = ['Brandname1', 'Brandname2', 'Brandname3']
        # Action
        result = get_unique(input_data)
        # Verify
        self.assertEqual(result, expected)

    def test_empty_list_returns_none(self):
        # Setup
        input_data = []
        # Action
        result = get_unique(input_data)
        # Verify
        self.assertIsNone(result)

    def test_all_invalid_brands_return_none(self):
        # Setup
        input_data = [{'brand': None}, {'brand': ''}, {'brand': ' '}, {'brand': None}]
        # Action
        result = get_unique(input_data)
        # Verify
        self.assertIsNone(result)

    def test_mixed_duplicates_and_blanks(self):
        # Setup
        input_data = [
            {'brand': 'Brandname'},
            {'brand': 'BrAnDNAme'},
            {'brand': 'BRANDNAME'},
            {'brand': 'brandname'},
            {'brand': None},
            {'brand': ' '}
        ]
        expected = ['Brandname']
        # Action
        result = get_unique(input_data)
        # Verify
        self.assertEqual(result, expected)

    def test_case_insensitivity_and_capitalization(self):
        # Setup
        input_data = [
            {'brand': 'apple'},
            {'brand': 'APPLE'},
            {'brand': 'Apple'},
            {'brand': 'aPpLe'}
        ]
        expected = ['Apple']
        # Action
        result = get_unique(input_data)
        # Verify
        self.assertEqual(result, expected)

    def test_preserves_order_of_first_occurrence(self):
        # Setup
        input_data = [
            {'brand': 'nike'},
            {'brand': 'Adidas'},
            {'brand': 'NIKE'},
            {'brand': 'adidas'},
            {'brand': 'Puma'}
        ]
        expected = ['Nike', 'Adidas', 'Puma']
        # Action
        result = get_unique(input_data)
        # Verify
        self.assertEqual(result, expected)

    def test_brands_with_leading_and_trailing_spaces(self):
        # Setup
        input_data = [
            {'brand': '  sony  '},
            {'brand': 'Sony'},
            {'brand': 'SONY '},
            {'brand': '  sony'}
        ]
        expected = ['Sony']
        # Action
        result = get_unique(input_data)
        # Verify
        self.assertEqual(result, expected)

    def test_brands_with_only_spaces_are_filtered_out(self):
        # Setup
        input_data = [
            {'brand': '   '},
            {'brand': '\t'},
            {'brand': '\n'},
            {'brand': 'ValidBrand'}
        ]
        expected = ['Validbrand']
        # Action
        result = get_unique(input_data)
        # Verify
        self.assertEqual(result, expected)

    def test_single_valid_brand(self):
        # Setup
        input_data = [{'brand': 'UniqueBrand'}]
        expected = ['Uniquebrand']
        # Action
        result = get_unique(input_data)
        # Verify
        self.assertEqual(result, expected)

    def test_multiple_none_and_empty_with_one_valid(self):
        # Setup
        input_data = [{'brand': None}, {'brand': ''}, {'brand': 'ValidBrand'}, {'brand': None}]
        expected = ['Validbrand']
        # Action
        result = get_unique(input_data)
        # Verify
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()