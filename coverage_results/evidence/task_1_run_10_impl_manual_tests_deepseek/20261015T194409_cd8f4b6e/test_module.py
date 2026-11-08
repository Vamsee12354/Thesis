import unittest
from implementation_manual import get_unique

class TestGetUnique(unittest.TestCase):
    def test_normal_case(self):
        input_list = [{'brand':'Brandname1'}, {'brand':'Brandname2'}, {'brand':'Brandname3'}]
        expected = ['Brandname1', 'Brandname2', 'Brandname3']
        self.assertEqual(get_unique(input_list), expected)

    def test_empty_list(self):
        self.assertIsNone(get_unique([]))

    def test_none_values(self):
        input_list = [{'brand':None}, {'brand':None}]
        self.assertIsNone(get_unique(input_list))

    def test_empty_strings(self):
        input_list = [{'brand':''}, {'brand':' '}]
        self.assertIsNone(get_unique(input_list))

    def test_mixed_invalid(self):
        input_list = [{'brand':None}, {'brand':''}, {'brand':' '}]
        self.assertIsNone(get_unique(input_list))

    def test_case_insensitive_deduplication(self):
        input_list = [{'brand':'Brandname'}, {'brand':'BrAnDNAme'}, {'brand':'BRANDNAME'}, {'brand':'brandname'}]
        expected = ['Brandname']
        self.assertEqual(get_unique(input_list), expected)

    def test_mixed_valid_invalid(self):
        input_list = [{'brand':'Valid1'}, {'brand':None}, {'brand':'VALID2'}, {'brand':' '}, {'brand':'valid1'}]
        expected = ['Valid1', 'Valid2']
        self.assertEqual(get_unique(input_list), expected)

    def test_single_valid(self):
        input_list = [{'brand':'SingleBrand'}]
        expected = ['SingleBrand']
        self.assertEqual(get_unique(input_list), expected)

    def test_preserve_order(self):
        input_list = [{'brand':'First'}, {'brand':'Second'}, {'brand':'first'}]
        expected = ['First', 'Second']
        self.assertEqual(get_unique(input_list), expected)