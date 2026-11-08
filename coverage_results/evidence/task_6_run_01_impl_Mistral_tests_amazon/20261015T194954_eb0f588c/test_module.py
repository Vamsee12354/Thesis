from unittest import TestCase
from implementation_manual import IsValidPassword

class TestPasswordValidator(TestCase):
    def test_missing_password(self):
        self.assertEqual(IsValidPassword(""), ["Please fill the password"])

    def test_password_too_short(self):
        self.assertEqual(IsValidPassword("short"), ["Length must be between 12 and 72 characters", "Password must contain an uppercase letter", "Password must contain a special character or a number"])

    def test_password_too_long(self):
        self.assertEqual(IsValidPassword("a" * 73), ["Length must be between 12 and 72 characters"])

    def test_no_lowercase_letter(self):
        self.assertEqual(IsValidPassword("A1!"), ["Password must contain a lowercase letter"])

    def test_no_uppercase_letter(self):
        self.assertEqual(IsValidPassword("a1!"), ["Password must contain an uppercase letter"])

    def test_no_special_character_or_number(self):
        self.assertEqual(IsValidPassword("abcdefABC"), ["Password must contain a special character or a number"])

    def test_valid_password(self):
        self.assertEqual(IsValidPassword("Abcdefg1!hij"), "The password is valid")

    def test_multiple_errors(self):
        self.assertEqual(IsValidPassword("short"), ["Length must be between 12 and 72 characters", "Password must contain an uppercase letter", "Password must contain a special character or a number"])