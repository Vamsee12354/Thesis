import unittest
from implementation_manual import get_unique

class TestGetUnique(unittest.TestCase):
    def test_normal_case(self):
        input_data = [{'brand': 'Brandname1'}, {'brand': 'Brandname2'}, {'brand': 'Brandname3'}]
        expected_output = ['Brandname1', 'Brandname2', 'Brandname3']
        self.assertEqual(get_unique(input_data), expected_output)

    def test_empty_list(self):
        input_data = []
        self.assertIsNone(get_unique(input_data))

    def test_all_invalid_brands(self):
        input_data = [{'brand': None}, {'brand': ''}, {'brand': ' '}]
        self.assertIsNone(get_unique(input_data))

    def test_mixed_case_duplicates(self):
        input_data = [{'brand': 'Brandname'}, {'brand': 'BrAnDNAme'}, {'brand': 'BRANDNAME'}, {'brand': 'brandname'}, {'brand': None}, {'brand': ' '}]
        expected_output = ['Brandname']
        self.assertEqual(get_unique(input_data), expected_output)

    def test_case_insensitivity(self):
        input_data = [{'brand': 'brandname'}, {'brand': 'BRANDNAME'}, {'brand': 'BrandName'}]
        expected_output = ['Brandname']
        self.assertEqual(get_unique(input_data), expected_output)

    def test_empty_strings_and_none(self):
        input_data = [{'brand': ''}, {'brand': None}, {'brand': ' '}]
        self.assertIsNone(get_unique(input_data))

    def test_single_valid_brand(self):
        input_data = [{'brand': 'Brandname'}]
        expected_output = ['Brandname']
        self.assertEqual(get_unique(input_data), expected_output)

    def test_multiple_duplicates(self):
        input_data = [{'brand': 'Brandname'}, {'brand': 'Brandname'}, {'brand': 'Brandname'}]
        expected_output = ['Brandname']
        self.assertEqual(get_unique(input_data), expected_output)

    def test_mixed_valid_and_invalid(self):
        input_data = [{'brand': 'Brandname1'}, {'brand': None}, {'brand': 'Brandname2'}, {'brand': ''}]
        expected_output = ['Brandname1', 'Brandname2']
        self.assertEqual(get_unique(input_data), expected_output)

    def test_no_brand_key(self):
        input_data = [{'name': 'Product1'}, {'name': 'Product2'}]
        self.assertIsNone(get_unique(input_data))

if __name__ == '__main__':
    unittest.main()