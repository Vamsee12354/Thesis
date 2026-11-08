import unittest
from implementation_manual import IsValidPassword

class TestPasswordValidator(unittest.TestCase):
    def test_missing_password(self):
        self.assertEqual(IsValidPassword(""), ["Please fill the password"])

    def test_password_too_short(self):
        self.assertEqual(IsValidPassword("Short1!"), ["Length must be between 12 and 72 characters"])

    def test_password_too_long(self):
        long_password = "a" * 73
        self.assertEqual(IsValidPassword(long_password), ["Length must be between 12 and 72 characters"])

    def test_password_missing_lowercase(self):
        password = "UPPERCASE123!"
        self.assertIn("Password must contain a lowercase letter", IsValidPassword(password))

    def test_password_missing_uppercase(self):
        password = "lowercase123!"
        self.assertIn("Password must contain an uppercase letter", IsValidPassword(password))

    def test_password_missing_special_char_or_number(self):
        password = "NoSpecialChars"
        self.assertIn("Password must contain a special character or a number", IsValidPassword(password))

    def test_multiple_errors(self):
        password = "short"
        result = IsValidPassword(password)
        self.assertIn("Length must be between 12 and 72 characters", result)
        self.assertIn("Password must contain an uppercase letter", result)
        self.assertIn("Password must contain a special character or a number", result)

    def test_valid_password(self):
        password = "ValidPassword123!"
        self.assertEqual(IsValidPassword(password), "The password is valid")

    def test_valid_password_with_min_length(self):
        password = "MinLength12!"
        self.assertEqual(IsValidPassword(password), "The password is valid")

    def test_valid_password_with_max_length(self):
        password = "A" * 70 + "a1!"
        self.assertEqual(IsValidPassword(password), "The password is valid")

    def test_password_with_only_numbers(self):
        password = "123456789012"
        self.assertIn("Password must contain a lowercase letter", IsValidPassword(password))
        self.assertIn("Password must contain an uppercase letter", IsValidPassword(password))

    def test_password_with_only_special_chars(self):
        password = "!@#$%^&*()_+"
        self.assertIn("Password must contain a lowercase letter", IsValidPassword(password))
        self.assertIn("Password must contain an uppercase letter", IsValidPassword(password))
        self.assertIn("Password must contain a special character or a number", IsValidPassword(password))