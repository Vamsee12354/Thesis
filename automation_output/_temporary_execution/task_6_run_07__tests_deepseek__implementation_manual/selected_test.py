import unittest
from implementation_manual import IsValidPassword

class TestIsValidPassword(unittest.TestCase):

    def test_missing_password(self):
        self.assertEqual(IsValidPassword(""), ["Please fill the password"])

    def test_password_too_short(self):
        self.assertEqual(IsValidPassword("short"), ["Length must be between 12 and 72 characters"])

    def test_password_too_long(self):
        self.assertEqual(IsValidPassword("a" * 73), ["Length must be between 12 and 72 characters"])

    def test_password_missing_lowercase(self):
        self.assertEqual(IsValidPassword("UPPERCASE123!"), ["Password must contain a lowercase letter"])

    def test_password_missing_uppercase(self):
        self.assertEqual(IsValidPassword("lowercase123!"), ["Password must contain an uppercase letter"])

    def test_password_missing_special_char_or_number(self):
        self.assertEqual(IsValidPassword("LowerUpper"), ["Password must contain a special character or a number"])

    def test_password_valid(self):
        self.assertEqual(IsValidPassword("ValidPassword123!"), "The password is valid")

    def test_multiple_errors(self):
        self.assertEqual(IsValidPassword("short"), ["Length must be between 12 and 72 characters"])

    def test_all_errors(self):
        self.assertEqual(IsValidPassword(""), ["Please fill the password"])

    def test_password_with_only_lowercase(self):
        self.assertEqual(IsValidPassword("lowercaseonly"), ["Length must be between 12 and 72 characters", "Password must contain an uppercase letter", "Password must contain a special character or a number"])

    def test_password_with_only_uppercase(self):
        self.assertEqual(IsValidPassword("UPPERCASEONLY"), ["Length must be between 12 and 72 characters", "Password must contain a lowercase letter", "Password must contain a special character or a number"])

    def test_password_with_only_numbers(self):
        self.assertEqual(IsValidPassword("123456789012"), ["Password must contain a lowercase letter", "Password must contain an uppercase letter"])

    def test_password_with_only_special_chars(self):
        self.assertEqual(IsValidPassword("!@#$%^&*()_+"), ["Password must contain a lowercase letter", "Password must contain an uppercase letter"])

    def test_password_with_lowercase_and_uppercase(self):
        self.assertEqual(IsValidPassword("LowerUpper"), ["Length must be between 12 and 72 characters", "Password must contain a special character or a number"])

    def test_password_with_lowercase_and_numbers(self):
        self.assertEqual(IsValidPassword("lowercase123"), ["Length must be between 12 and 72 characters", "Password must contain an uppercase letter"])

    def test_password_with_uppercase_and_numbers(self):
        self.assertEqual(IsValidPassword("UPPERCASE123"), ["Length must be between 12 and 72 characters", "Password must contain a lowercase letter"])

    def test_password_with_lowercase_and_special_chars(self):
        self.assertEqual(IsValidPassword("lowercase!@#"), ["Length must be between 12 and 72 characters", "Password must contain an uppercase letter"])

    def test_password_with_uppercase_and_special_chars(self):
        self.assertEqual(IsValidPassword("UPPERCASE!@#"), ["Length must be between 12 and 72 characters", "Password must contain a lowercase letter"])

    def test_password_with_numbers_and_special_chars(self):
        self.assertEqual(IsValidPassword("123!@#"), ["Length must be between 12 and 72 characters", "Password must contain a lowercase letter", "Password must contain an uppercase letter"])

    def test_password_with_lowercase_uppercase_and_numbers(self):
        self.assertEqual(IsValidPassword("LowerUpper123"), ["Length must be between 12 and 72 characters", "Password must contain a special character or a number"])

    def test_password_with_lowercase_uppercase_and_special_chars(self):
        self.assertEqual(IsValidPassword("LowerUpper!@#"), ["Length must be between 12 and 72 characters", "Password must contain a special character or a number"])

    def test_password_with_lowercase_numbers_and_special_chars(self):
        self.assertEqual(IsValidPassword("lowercase123!@#"), ["Length must be between 12 and 72 characters", "Password must contain an uppercase letter"])

    def test_password_with_uppercase_numbers_and_special_chars(self):
        self.assertEqual(IsValidPassword("UPPERCASE123!@#"), ["Length must be between 12 and 72 characters", "Password must contain a lowercase letter"])

    def test_password_with_all_requirements(self):
        self.assertEqual(IsValidPassword("ValidPassword123!"), "The password is valid")