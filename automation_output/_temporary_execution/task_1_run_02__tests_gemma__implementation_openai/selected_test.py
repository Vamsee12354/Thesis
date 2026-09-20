import unittest
from implementation_manual import get_unique

class TestGetUnique(unittest.TestCase):

    def test_normal_case_with_valid_brands(self):
        # Setup
        brands = [{'brand': 'Brandname1'}, {'brand': 'Brandname2'}, {'brand': 'Brandname3'}]
        expected = ['Brandname1', 'Brandname2', 'Brandname3']
        
        # Action
        result = get_unique(*brands)
        
        # Verification
        self.assertEqual(result, expected)

    def test_empty_input_returns_none(self):
        # Setup
        brands = []
        
        # Action
        result = get_unique(*brands)
        
        # Verification
        self.assertIsNone(result)

    def test_all_invalid_brands_returns_none(self):
        # Setup
        brands = [{'brand': None}, {'brand': ''}, {'brand': ' '}]
        
        # Action
        result = get_unique(*brands)
        
        # Verification
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
        result = get_unique(*brands)
        
        # Verification
        self.assertEqual(result, expected)

    def test_case_insensitivity_and_normalization(self):
        # Setup
        brands = [{'brand': 'apple'}, {'brand': 'APPLE'}, {'brand': '  Apple  '}]
        expected = ['Apple']
        
        # Action
        result = get_unique(*brands)
        
        # Verification
        self.assertEqual(result, expected)

    def test_preserves_order_of_first_appearance(self):
        # Setup
        brands = [
            {'brand': 'Nike'}, 
            {'brand': 'Adidas'}, 
            {'brand': 'nike'}, 
            {'brand': 'Adidas'}
        ]
        expected = ['Nike', 'Adidas']
        
        # Action
        result = get_unique(*brands)
        
        # Verification
        self.assertEqual(result, expected)

    def test_single_valid_brand(self):
        # Setup
        brands = [{'brand': 'Sony'}]
        expected = ['Sony']
        
        # Action
        result = get_unique(*brands)
        
        # Verification
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()