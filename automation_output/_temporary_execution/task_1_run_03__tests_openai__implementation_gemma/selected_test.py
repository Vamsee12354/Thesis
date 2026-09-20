import unittest
from implementation_manual import get_unique

class TestGetUniqueBrands(unittest.TestCase):

    def test_normal_case_with_valid_brands(self):
        # Setup
        brands = [{'brand': 'Brandname1'}, {'brand': 'Brandname2'}, {'brand': 'Brandname3'}]
        expected = ['Brandname1', 'Brandname2', 'Brandname3']
        # Action
        result = get_unique(brands)
        # Verify
        self.assertEqual(result, expected)

    def test_empty_list_returns_none(self):
        # Setup
        brands = []
        # Action
        result = get_unique(brands)
        # Verify
        self.assertIsNone(result)

    def test_all_invalid_or_missing_brands(self):
        # Setup
        brands = [{'brand': None}, {'brand': ''}, {'brand': ' '}, {'brand': None}]
        # Action
        result = get_unique(brands)
        # Verify
        self.assertIsNone(result)

    def test_mixed_duplicates_and_blanks(self):
        # Setup
        brands = [
            {'brand': 'Brandname'},
            {'brand': 'BrAnDNAme'},
            {'brand': 'BRANDNAME'},
            {'brand': 'brandname'},
            {'brand': None},
            {'brand': ' '}
        ]
        expected = ['Brandname']
        # Action
        result = get_unique(brands)
        # Verify
        self.assertEqual(result, expected)

    def test_case_insensitivity_and_capitalization(self):
        # Setup
        brands = [
            {'brand': 'apple'},
            {'brand': 'Apple'},
            {'brand': 'APPLE'},
            {'brand': 'aPpLe'}
        ]
        expected = ['Apple']
        # Action
        result = get_unique(brands)
        # Verify
        self.assertEqual(result, expected)

    def test_multiple_unique_brands_with_varied_cases(self):
        # Setup
        brands = [
            {'brand': 'nike'},
            {'brand': 'Adidas'},
            {'brand': 'NIKE'},
            {'brand': 'adidas'},
            {'brand': 'Puma'},
            {'brand': 'puma'}
        ]
        expected = ['Nike', 'Adidas', 'Puma']
        # Action
        result = get_unique(brands)
        # Verify
        self.assertEqual(result, expected)

    def test_brands_with_leading_and_trailing_spaces(self):
        # Setup
        brands = [
            {'brand': '  Sony  '},
            {'brand': 'sony'},
            {'brand': ' SONY '},
            {'brand': '  sOnY'}
        ]
        expected = ['Sony']
        # Action
        result = get_unique(brands)
        # Verify
        self.assertEqual(result, expected)

    def test_brands_with_only_spaces_are_filtered_out(self):
        # Setup
        brands = [
            {'brand': '   '},
            {'brand': '  '},
            {'brand': ''}
        ]
        # Action
        result = get_unique(brands)
        # Verify
        self.assertIsNone(result)

    def test_single_valid_brand(self):
        # Setup
        brands = [{'brand': 'UniqueBrand'}]
        expected = ['Uniquebrand']
        # Action
        result = get_unique(brands)
        # Verify
        self.assertEqual(result, expected)

    def test_brands_with_non_string_values_ignored(self):
        # Setup
        brands = [
            {'brand': 'ValidBrand'},
            {'brand': 123},
            {'brand': None},
            {'brand': ['list']},
            {'brand': 'validbrand'}
        ]
        expected = ['Validbrand']
        # Action
        result = get_unique(brands)
        # Verify
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()