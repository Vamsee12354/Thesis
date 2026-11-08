import unittest
from implementation_manual import IsValidPassword

class TestPasswordValidator(unittest.TestCase):
    def test_missing_password(self):
        self.assertEqual(IsValidPassword(""), ["Please fill the password"])

    def test_password_too_short(self):
        self.assertEqual(IsValidPassword("Short1!"), ["Length must be between 12 and 72 characters"])

    def test_password_too_long(self):
        long_password = "a" * 73 + "A1!"
        self.assertEqual(IsValidPassword(long_password), ["Length must be between 12 and 72 characters"])

    def test_password_missing_lowercase(self):
        self.assertEqual(IsValidPassword("PASSWORD1234!"), ["Password must contain a lowercase letter"])

    def test_password_missing_uppercase(self):
        self.assertEqual(IsValidPassword("password1234!"), ["Password must contain an uppercase letter"])

    def test_password_missing_special_char_or_number(self):
        self.assertEqual(IsValidPassword("PasswordPassword"), ["Password must contain a special character or a number"])

    def test_multiple_errors(self):
        result = IsValidPassword("short")
        self.assertIn("Length must be between 12 and 72 characters", result)
        self.assertIn("Password must contain an uppercase letter", result)
        self.assertIn("Password must contain a special character or a number", result)

    def test_valid_password(self):
        self.assertEqual(IsValidPassword("ValidPassword123!"), "The password is valid")