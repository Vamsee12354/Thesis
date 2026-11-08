import unittest
from implementation_manual import get_unique

class TestGetUnique(unittest.TestCase):
    def test_normal_case_with_valid_brands(self):
        input_data = [{'brand': 'Brandname1'}, {'brand': 'Brandname2'}, {'brand': 'Brandname3'}]
        expected = ['Brandname1', 'Brandname2', 'Brandname3']
        self.assertEqual(get_unique(input_data), expected)

    def test_empty_input(self):
        self.assertIsNone(get_unique([]))

    def test_all_none_or_empty_brands(self):
        input_data = [{'brand': None}, {'brand': ''}, {'brand': ' '}]
        self.assertIsNone(get_unique(input_data))

    def test_case_insensitive_deduplication(self):
        input_data = [
            {'brand': 'Brandname'},
            {'brand': 'BrAnDNAme'},
            {'brand': 'BRANDNAME'},
            {'brand': 'brandname'},
            {'brand': None},
            {'brand': ' '}
        ]
        expected = ['Brandname']
        self.assertEqual(get_unique(input_data), expected)

    def test_mixed_valid_and_invalid(self):
        input_data = [
            {'brand': 'Valid1'},
            {'brand': None},
            {'brand': 'valid2'},
            {'brand': ''},
            {'brand': 'VALID1'},
            {'brand': ' '}
        ]
        expected = ['Valid1', 'Valid2']
        self.assertEqual(get_unique(input_data), expected)

    def test_single_valid_brand(self):
        input_data = [{'brand': 'SingleBrand'}]
        expected = ['SingleBrand']
        self.assertEqual(get_unique(input_data), expected)

    def test_all_duplicates(self):
        input_data = [
            {'brand': 'Duplicate'},
            {'brand': 'duplicate'},
            {'brand': 'DUPLICATE'}
        ]
        expected = ['Duplicate']
        self.assertEqual(get_unique(input_data), expected)

    def test_no_brand_key_raises_error(self):
        input_data = [{'not_brand': 'test'}]
        with self.assertRaises(KeyError):
            get_unique(input_data)