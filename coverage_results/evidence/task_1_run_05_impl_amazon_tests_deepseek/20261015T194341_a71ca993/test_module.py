import unittest
from implementation_manual import get_unique

class TestGetUnique(unittest.TestCase):
    def test_normal_case(self):
        input_data = [{'brand': 'Brandname1'}, {'brand': 'Brandname2'}, {'brand': 'Brandname3'}]
        expected_output = ['Brandname1', 'Brandname2', 'Brandname3']
        self.assertEqual(get_unique(input_data), expected_output)

    def test_all_invalid_brands(self):
        input_data = [{'brand': None}, {'brand': ''}, {'brand': ' '}]
        self.assertIsNone(get_unique(input_data))

    def test_empty_list(self):
        input_data = []
        self.assertIsNone(get_unique(input_data))

    def test_mixed_case_duplicates(self):
        input_data = [{'brand': 'Brandname'}, {'brand': 'BrAnDNAme'}, {'brand': 'BRANDNAME'}, {'brand': 'brandname'}, {'brand': None}, {'brand': ' '}]
        expected_output = ['Brandname']
        self.assertEqual(get_unique(input_data), expected_output)

    def test_case_insensitivity(self):
        input_data = [{'brand': 'brandname'}, {'brand': 'BRANDNAME'}, {'brand': 'BrandName'}]
        expected_output = ['Brandname']
        self.assertEqual(get_unique(input_data), expected_output)

    def test_no_duplicates(self):
        input_data = [{'brand': 'Brand1'}, {'brand': 'Brand2'}, {'brand': 'Brand3'}]
        expected_output = ['Brand1', 'Brand2', 'Brand3']
        self.assertEqual(get_unique(input_data), expected_output)

    def test_mixed_valid_invalid(self):
        input_data = [{'brand': 'Brand1'}, {'brand': None}, {'brand': 'Brand2'}, {'brand': ''}, {'brand': 'Brand3'}]
        expected_output = ['Brand1', 'Brand2', 'Brand3']
        self.assertEqual(get_unique(input_data), expected_output)

    def test_all_none(self):
        input_data = [{'brand': None}, {'brand': None}, {'brand': None}]
        self.assertIsNone(get_unique(input_data))

    def test_all_empty_strings(self):
        input_data = [{'brand': ''}, {'brand': ''}, {'brand': ''}]
        self.assertIsNone(get_unique(input_data))

    def test_all_spaces(self):
        input_data = [{'brand': ' '}, {'brand': ' '}, {'brand': ' '}]
        self.assertIsNone(get_unique(input_data))

if __name__ == '__main__':
    unittest.main()