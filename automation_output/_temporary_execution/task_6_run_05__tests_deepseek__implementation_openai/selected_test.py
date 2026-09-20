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
        self.assertEqual(IsValidPassword(password), ["Password must contain a lowercase letter"])

    def test_password_missing_uppercase(self):
        password = "lowercase123!"
        self.assertEqual(IsValidPassword(password), ["Password must contain an uppercase letter"])

    def test_password_missing_special_or_number(self):
        password = "NoSpecialChars"
        self.assertEqual(IsValidPassword(password), ["Password must contain a special character or a number"])

    def test_multiple_errors(self):
        password = "short"
        expected_errors = [
            "Length must be between 12 and 72 characters",
            "Password must contain an uppercase letter",
            "Password must contain a special character or a number"
        ]
        self.assertEqual(IsValidPassword(password), expected_errors)

    def test_valid_password(self):
        password = "ValidPassword123!"
        self.assertEqual(IsValidPassword(password), "The password is valid")

    def test_valid_password_with_special_chars(self):
        password = "AnotherValid!@#123"
        self.assertEqual(IsValidPassword(password), "The password is valid")

    def test_valid_password_max_length(self):
        password = "A" + "a" * 70 + "1!"
        self.assertEqual(IsValidPassword(password), "The password is valid")

    def test_valid_password_min_length(self):
        password = "Aa1!Aa1!Aa1!A"
        self.assertEqual(IsValidPassword(password), "The password is valid")