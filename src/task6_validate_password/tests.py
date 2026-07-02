# Tests for task6_validate_password
import unittest
from implementation_manual import is_valid_password

class Test_password_valid(unittest.TestCase):
    def test_no_password(self):
        self.assertEqual(is_valid_password(""),"Please fill the password")

    def test_no_lowercase(self):
        self.assertEqual(is_valid_password("ABCDEFGHIJK*1"),['Password must contain a lowercase letter'])
    
    def test_no_upprcase(self):
        self.assertEqual(is_valid_password("abcdefghijk*1"),['Password must contain an uppercase letter'])

    def test_no_symbols(self):
        self.assertEqual(is_valid_password("Abcdefghijkl1"),['Password must contain a special character or a number'])

    def test_lower_upper_no_symbol(self):
        self.assertEqual(is_valid_password("Abcdefghijkl1"),['Password must contain a special character or a number'])

    def test_nolower_upper_symbol(self):
        self.assertEqual(is_valid_password("ABCDEFGHIJK*1"),['Password must contain a lowercase letter'])

    def test_noupper_lower_symbol(self):
        self.assertEqual(is_valid_password("abcdefghijk*1"),['Password must contain an uppercase letter'])
    
    def test_diff_language(self):
        self.assertEqual(is_valid_password("అఆఇఅఆఇఅఆఇఅఆఇ*1Aa"),"The password is valid")

    def test_short_len_pwd(self):
        self.assertEqual(is_valid_password("Shean123*"),['Length must be between 12 and 72 characters'])
    
    def test_long_len_pwd(self):
        self.assertEqual(is_valid_password("Shean123*" + "a"*70),['Length must be between 12 and 72 characters'])

    def test_working_pwd(self):
        self.assertEqual(is_valid_password("Shean12354*ab"),"The password is valid")

    def test_mix_languages(self):
        self.assertEqual(is_valid_password("అఆఇఅఆఇ123loremipsumZZ*"),"The password is valid")

    def test_only_symbols(self):
        self.assertEqual(is_valid_password("!@#$%^&*()*!@"),['Password must contain a lowercase letter','Password must contain an uppercase letter','Password must contain a special character or a number'])

    def test_spaces_in_pwd(self):
        self.assertEqual(is_valid_password("Shean 12354*ab"),"The password is valid")

if __name__ == "__main__":
    unittest.main()