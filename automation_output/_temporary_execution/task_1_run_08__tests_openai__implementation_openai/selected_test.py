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

    def test_all_invalid_or_missing_brands_return_none(self):
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
            {'brand': 'Apple'},
            {'brand': 'APPLE'},
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
            {'brand': 'zeta'},
            {'brand': 'Alpha'},
            {'brand': 'beta'},
            {'brand': 'alpha'},
            {'brand': 'ZETA'},
            {'brand': 'Beta'}
        ]
        expected = ['Zeta', 'Alpha', 'Beta']
        # Action
        result = get_unique(input_data)
        # Verify
        self.assertEqual(result, expected)

    def test_brands_with_leading_and_trailing_spaces(self):
        # Setup
        input_data = [
            {'brand': '  nike'},
            {'brand': 'Nike  '},
            {'brand': '  NIKE  '},
            {'brand': 'adidas'},
            {'brand': ' Adidas '}
        ]
        expected = ['Nike', 'Adidas']
        # Action
        result = get_unique(input_data)
        # Verify
        self.assertEqual(result, expected)

    def test_brands_with_only_spaces_are_filtered_out(self):
        # Setup
        input_data = [
            {'brand': '   '},
            {'brand': '  '},
            {'brand': ''}
        ]
        # Action
        result = get_unique(input_data)
        # Verify
        self.assertIsNone(result)

    def test_single_valid_brand(self):
        # Setup
        input_data = [{'brand': 'UniqueBrand'}]
        expected = ['Uniquebrand']
        # Action
        result = get_unique(input_data)
        # Verify
        self.assertEqual(result, expected)

    def test_multiple_none_and_valid_brands(self):
        # Setup
        input_data = [
            {'brand': None},
            {'brand': 'ValidBrand'},
            {'brand': None},
            {'brand': 'validbrand'},
            {'brand': ''}
        ]
        expected = ['Validbrand']
        # Action
        result = get_unique(input_data)
        # Verify
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()