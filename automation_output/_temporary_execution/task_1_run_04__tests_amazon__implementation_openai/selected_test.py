import unittest
from implementation_manual import get_unique

class TestGetUnique(unittest.TestCase):

    def test_normal_case_with_valid_brands(self):
        self.assertEqual(get_unique([{'brand':'Brandname1'}, {'brand':'Brandname2'}, {'brand':'Brandname3'}]), 
                         ['Brandname1', 'Brandname2', 'Brandname3'])

    def test_only_invalid_or_missing_brands(self):
        self.assertIsNone(get_unique([]))
        self.assertIsNone(get_unique([{'brand': None}, {'brand': ''}]))

    def test_mixed_with_duplicates_and_blanks(self):
        self.assertEqual(get_unique([{'brand':'Brandname'}, {'brand':'BrAnDNAme'}, {'brand':'BRANDNAME'}, {'brand':'brandname'},{'brand':None}, {'brand':''}]), 
                         ['Brandname'])

    def test_case_insensitivity(self):
        self.assertEqual(get_unique([{'brand':'Brandname'}, {'brand':'BRANDNAME'}]), 
                         ['Brandname'])

    def test_empty_string_filtered_out(self):
        self.assertEqual(get_unique([{'brand':'Brandname'}, {'brand':''}]), 
                         ['Brandname'])

    def test_none_filtered_out(self):
        self.assertEqual(get_unique([{'brand':'Brandname'}, {'brand':None}]), 
                         ['Brandname'])

if __name__ == '__main__':
    unittest.main()
