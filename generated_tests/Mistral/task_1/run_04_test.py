from implementation_manual import get_unique
import unittest

class TestGetUnique(unittest.TestCase):

    def test_normal_case_with_valid_brands(self):
        input_list = [{'brand': 'Brandname1'}, {'brand': 'Brandname2'}, {'brand': 'Brandname3'}]
        result = get_unique(input_list)
        self.assertEqual(result, ['Brandname1', 'Brandname2', 'Brandname3'])

    def test_empty_list(self):
        input_list = []
        result = get_unique(input_list)
        self.assertIsNone(result)

    def test_all_invalid_brands(self):
        input_list = [{'brand': None}, {'brand': ''}, {'brand': ' '}]
        result = get_unique(input_list)
        self.assertIsNone(result)

    def test_mixed_with_duplicates_and_blanks(self):
        input_list = [
            {'brand': 'Brandname'},
            {'brand': 'BrAnDNAme'},
            {'brand': 'BRANDNAME'},
            {'brand': 'brandname'},
            {'brand': None},
            {'brand': ' '}
        ]
        result = get_unique(input_list)
        self.assertEqual(result, ['Brandname'])

    def test_case_insensitive_duplicates(self):
        input_list = [
            {'brand': 'apple'},
            {'brand': 'Apple'},
            {'brand': 'APPLE'},
            {'brand': 'Banana'}
        ]
        result = get_unique(input_list)
        self.assertEqual(result, ['Apple', 'Banana'])

    def test_single_valid_brand(self):
        input_list = [{'brand': 'Samsung'}]
        result = get_unique(input_list)
        self.assertEqual(result, ['Samsung'])

    def test_single_invalid_brand(self):
        input_list = [{'brand': None}]
        result = get_unique(input_list)
        self.assertIsNone(result)

    def test_whitespace_only_brand(self):
        input_list = [{'brand': '   '}]
        result = get_unique(input_list)
        self.assertIsNone(result)

    def test_mixed_valid_and_invalid_brands(self):
        input_list = [
            {'brand': 'Nike'},
            {'brand': ''},
            {'brand': 'adidas'},
            {'brand': None},
            {'brand': 'Puma'}
        ]
        result = get_unique(input_list)
        self.assertEqual(result, ['Nike', 'Adidas', 'Puma'])

    def test_all_same_brand_case_variations(self):
        input_list = [
            {'brand': 'toyota'},
            {'brand': 'TOYOTA'},
            {'brand': 'Toyota'},
            {'brand': 'toYOTa'}
        ]
        result = get_unique(input_list)
        self.assertEqual(result, ['Toyota'])