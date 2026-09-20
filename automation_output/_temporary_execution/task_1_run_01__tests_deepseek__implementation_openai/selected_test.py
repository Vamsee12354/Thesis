import unittest
from implementation_manual import get_unique

class TestGetUniqueBrands(unittest.TestCase):
    def test_normal_case_with_valid_brands(self):
        input_data = [{'brand': 'Brandname1'}, {'brand': 'Brandname2'}, {'brand': 'Brandname3'}]
        expected = ['Brandname1', 'Brandname2', 'Brandname3']
        self.assertEqual(get_unique(*input_data), expected)

    def test_empty_input(self):
        self.assertIsNone(get_unique([]))
        
    def test_all_invalid_brands(self):
        input_data = [{'brand': None}, {'brand': ''}, {'brand': ' '}]
        self.assertIsNone(get_unique(*input_data))

    def test_case_insensitive_deduplication(self):
        input_data = [
            {'brand':'Brandname'}, 
            {'brand':'BrAnDNAme'}, 
            {'brand':'BRANDNAME'}, 
            {'brand':'brandname'},
            {'brand':None}, 
            {'brand': ' '}
        ]
        expected = ['Brandname']
        self.assertEqual(get_unique(*input_data), expected)

    def test_mixed_valid_and_invalid(self):
        input_data = [
            {'brand': 'Valid1'},
            {'brand': ''},
            {'brand': 'VALID2'},
            {'brand': None},
            {'brand': 'valid1'},
            {'brand': ' '},
            {'brand': 'AnotherBrand'}
        ]
        expected = ['Valid1', 'Valid2', 'AnotherBrand']
        self.assertEqual(get_unique(*input_data), expected)

    def test_no_valid_brands_empty_list(self):
        self.assertIsNone(get_unique([]))

    def test_single_valid_brand(self):
        input_data = [{'brand': 'SingleBrand'}]
        expected = ['SingleBrand']
        self.assertEqual(get_unique(*input_data), expected)

    def test_all_identical_brands(self):
        input_data = [{'brand': 'Same'}, {'brand': 'Same'}, {'brand': 'SAME'}]
        expected = ['Same']
        self.assertEqual(get_unique(*input_data), expected)