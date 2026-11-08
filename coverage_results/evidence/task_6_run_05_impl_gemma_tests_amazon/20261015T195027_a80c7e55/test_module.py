from unittest import TestCase
from implementation_manual import IsValidPassword

class TestIsValidPassword(TestCase):
    def test_missing_password(self):
        self.assertEqual(IsValidPassword(""), ["Please fill the password"])

    def test_password_too_short(self):
        self.assertEqual(IsValidPassword("short"), ["Length must be between 12 and 72 characters", "Password must contain an uppercase letter", "Password must contain a special character or a number"])

    def test_password_too_long(self):
        self.assertEqual(IsValidPassword("a" * 73), ["Length must be between 12 and 72 characters"])

    def test_no_lowercase_letter(self):
        self.assertEqual(IsValidPassword("ABC123!"), ["Password must contain a lowercase letter"])

    def test_no_uppercase_letter(self):
        self.assertEqual(IsValidPassword("abc123!"), ["Password must contain an uppercase letter"])

    def test_no_special_character_or_number(self):
        self.assertEqual(IsValidPassword("abcABC"), ["Password must contain a special character or a number"])

    def test_strong_password(self):
        self.assertEqual(IsValidPassword("aBcD123!@#"), "The password is valid")

    def test_multiple_errors(self):
        self.assertEqual(IsValidPassword("short"), ["Length must be between 12 and 72 characters", "Password must contain an uppercase letter", "Password must contain a special character or a number"])