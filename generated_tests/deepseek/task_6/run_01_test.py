import unittest
from implementation_manual import IsValidPassword

class TestPasswordValidator(unittest.TestCase):
    def test_empty_password(self):
        self.assertEqual(IsValidPassword(""), ["Please fill the password"])

    def test_none_password(self):
        self.assertEqual(IsValidPassword(None), ["Please fill the password"])

    def test_short_password(self):
        self.assertEqual(IsValidPassword("Short1!"), ["Length must be between 12 and 72 characters"])

    def test_long_password(self):
        long_pwd = "a" * 73
        self.assertEqual(IsValidPassword(long_pwd), ["Length must be between 12 and 72 characters"])

    def test_missing_lowercase(self):
        pwd = "UPPERCASE123!"
        self.assertEqual(IsValidPassword(pwd), ["Password must contain a lowercase letter"])

    def test_missing_uppercase(self):
        pwd = "lowercase123!"
        self.assertEqual(IsValidPassword(pwd), ["Password must contain an uppercase letter"])

    def test_missing_special_or_number(self):
        pwd = "LowerUpper"
        self.assertEqual(IsValidPassword(pwd), ["Password must contain a special character or a number"])

    def test_multiple_errors(self):
        pwd = "short"
        expected_errors = [
            "Length must be between 12 and 72 characters",
            "Password must contain an uppercase letter",
            "Password must contain a special character or a number"
        ]
        self.assertEqual(IsValidPassword(pwd), expected_errors)

    def test_valid_password(self):
        pwd = "ValidPassword123!"
        self.assertEqual(IsValidPassword(pwd), "The password is valid")

    def test_valid_password_with_special_chars(self):
        pwd = "AnotherValid@123"
        self.assertEqual(IsValidPassword(pwd), "The password is valid")

    def test_valid_long_password(self):
        pwd = "A" + "a" * 10 + "1!"
        self.assertEqual(IsValidPassword(pwd), "The password is valid")

    def test_valid_max_length_password(self):
        pwd = "A" + "a" * 70 + "1!"
        self.assertEqual(IsValidPassword(pwd), "The password is valid")