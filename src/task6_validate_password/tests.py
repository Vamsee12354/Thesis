# Tests for task6_validate_password
import unittest
from implementation_manual import IsValidPassword


class Test_password_valid(unittest.TestCase):
    def test_no_password(self):
        self.assertEqual(IsValidPassword(""),False)

    def test_no_lowercase(self):
        self.assertEqual(IsValidPassword("ABCDEFG*"),False)
    
    def test_no_upprcase(self):
        self.assertEqual(IsValidPassword("abcdefg*"),False)

    def test_no_symbols(self):
        self.assertEqual(IsValidPassword("Abcdefg"),False)

    def test_lower_upper_no_symbol(self):
        self.assertEqual(IsValidPassword("Abcdefg"),False)

    def test_nolower_upper_symbol(self):
        self.assertEqual(IsValidPassword("ABCDEFG*"),False)

    def test_noupper_lower_symbol(self):
        self.assertEqual(IsValidPassword("abcdefg*"),False)
    
    def test_diff_language(self):
        self.assertEqual(IsValidPassword("అఆఇఅఆఇ*"),False)

    def test_short_len_pwd(self):
        self.assertEqual(IsValidPassword("ABC*"),False)
    
    def test_long_len_pwd(self):
        self.assertEqual(IsValidPassword("LoremipsumdolorsitWertex*"),False)

    def test_working_pwd(self):
        self.assertEqual(IsValidPassword("Shean12354*"),True)

    def test_mix_languages(self):
        self.assertEqual(IsValidPassword("అఆఇఅఆఇ123loremipsumZZ*"),True)

    def test_only_symbols(self):
        self.assertEqual(IsValidPassword("!@#$%^&*()*"),False)

    def test_spaces_in_pwd(self):
        self.assertEqual(IsValidPassword("Shean 12354*"),True)

    

    


if __name__ == "__main__":
    unittest.main()