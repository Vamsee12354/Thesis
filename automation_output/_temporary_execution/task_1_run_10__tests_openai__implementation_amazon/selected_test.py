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

    def test_brands_with_leading_and_trailing_spaces(self):
        # Setup
        input_data = [
            {'brand': '  Nike'},
            {'brand': 'nike  '},
            {'brand': '  NIKE  '}
        ]
        expected = ['Nike']
        # Action
        result = get_unique(input_data)
        # Verify
        self.assertEqual(result, expected)

    def test_multiple_unique_brands_with_varied_cases_and_spaces(self):
        # Setup
        input_data = [
            {'brand': 'Adidas'},
            {'brand': 'adidas'},
            {'brand': '  Puma'},
            {'brand': 'PUMA  '},
            {'brand': 'Reebok'},
            {'brand': 'reebok'},
            {'brand': None},
            {'brand': ''}
        ]
        expected = ['Adidas', 'Puma', 'Reebok']
        # Action
        result = get_unique(input_data)
        # Verify
        self.assertEqual(result, expected)

    def test_single_valid_brand(self):
        # Setup
        input_data = [{'brand': 'Sony'}]
        expected = ['Sony']
        # Action
        result = get_unique(input_data)
        # Verify
        self.assertEqual(result, expected)

    def test_single_invalid_brand_none(self):
        # Setup
        input_data = [{'brand': None}]
        # Action
        result = get_unique(input_data)
        # Verify
        self.assertIsNone(result)

    def test_single_invalid_brand_empty_string(self):
        # Setup
        input_data = [{'brand': ''}]
        # Action
        result = get_unique(input_data)
        # Verify
        self.assertIsNone(result)

    def test_brands_with_internal_spaces_and_mixed_cases(self):
        # Setup
        input_data = [
            {'brand': 'New Brand'},
            {'brand': 'new brand'},
            {'brand': 'NEW BRAND'},
            {'brand': 'New  Brand'},
            {'brand': '  New Brand  '}
        ]
        expected = ['New brand']
        # Action
        result = get_unique(input_data)
        # Verify
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()