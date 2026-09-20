import unittest
from implementation_manual import IsValidPassword

class TestIsValidPassword(unittest.TestCase):
    def test_missing_password(self):
        self.assertEqual(IsValidPassword(""), ["Please fill the password"])

    def test_password_too_short(self):
        self.assertEqual(IsValidPassword("short"), ["Length must be between 12 and 72 characters"])

    def test_password_too_long(self):
        long_password = "a" * 73
        self.assertEqual(IsValidPassword(long_password), ["Length must be between 12 and 72 characters"])

    def test_password_missing_lowercase(self):
        password = "PASSWORD123!"
        self.assertEqual(IsValidPassword(password), ["Password must contain a lowercase letter"])

    def test_password_missing_uppercase(self):
        password = "password123!"
        self.assertEqual(IsValidPassword(password), ["Password must contain an uppercase letter"])

    def test_password_missing_special_char_or_number(self):
        password = "PasswordPassword"
        self.assertEqual(IsValidPassword(password), ["Password must contain a special character or a number"])

    def test_multiple_errors(self):
        password = "short"
        self.assertEqual(IsValidPassword(password), [
            "Length must be between 12 and 72 characters",
            "Password must contain an uppercase letter",
            "Password must contain a special character or a number"
        ])

    def test_valid_password(self):
        password = "ValidPassword123!"
        self.assertEqual(IsValidPassword(password), "The password is valid")

    def test_valid_password_with_special_char(self):
        password = "ValidPassword!"
        self.assertEqual(IsValidPassword(password), "The password is valid")

    def test_valid_password_with_number(self):
        password = "ValidPassword123"
        self.assertEqual(IsValidPassword(password), "The password is valid")

    def test_valid_password_min_length(self):
        password = "ValidPass123"
        self.assertEqual(IsValidPassword(password), "The password is valid")

    def test_valid_password_max_length(self):
        password = "a" * 72
        self.assertEqual(IsValidPassword(password), "The password is valid")