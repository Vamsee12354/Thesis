import unittest
from implementation_manual import get_unique

class TestGetUnique(unittest.TestCase):

    def test_get_unique_normal_case(self):
        # Setup
        brands = [{'brand': 'Brandname1'}, {'brand': 'Brandname2'}, {'brand': 'Brandname3'}]
        expected = ['Brandname1', 'Brandname2', 'Brandname3']
        
        # Action
        result = get_unique(brands)
        
        # Verification
        self.assertEqual(result, expected)

    def test_get_unique_empty_input(self):
        # Setup
        brands = []
        expected = None
        
        # Action
        result = get_unique(brands)
        
        # Verification
        self.assertIsNone(result)

    def test_get_unique_all_invalid_values(self):
        # Setup
        brands = [{'brand': None}, {'brand': ''}, {'brand': ' '}]
        expected = None
        
        # Action
        result = get_unique(brands)
        
        # Verification
        self.assertIsNone(result)

    def test_get_unique_mixed_duplicates_and_blanks(self):
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
        
        # Verification
        self.assertEqual(result, expected)

    def test_get_unique_case_insensitivity_and_normalization(self):
        # Setup
        brands = [{'brand': 'apple'}, {'brand': 'APPLE'}, {'brand': '  Apple  '}]
        expected = ['Apple']
        
        # Action
        result = get_unique(brands)
        
        # Verification
        self.assertEqual(result, expected)

    def test_get_unique_preserves_order_of_first_appearance(self):
        # Setup
        # The requirement says "Do not sort the final output list"
        # We test that it maintains the order of the first valid occurrence
        brands = [{'brand': 'Zebra'}, {'brand': 'Apple'}, {'brand': 'zebra'}]
        expected = ['Zebra', 'Apple']
        
        # Action
        result = get_unique(brands)
        
        # Verification
        self.assertEqual(result, expected)

    def test_get_unique_with_whitespace_only_strings(self):
        # Setup
        # "removes any None or empty string values" 
        # "normalize them to a capitalized format"
        # A string of spaces " " becomes "" after strip, which should be filtered
        brands = [{'brand': '  '}, {'brand': 'Valid'}]
        expected = ['Valid']
        
        # Action
        result = get_unique(brands)
        
        # Verification
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()