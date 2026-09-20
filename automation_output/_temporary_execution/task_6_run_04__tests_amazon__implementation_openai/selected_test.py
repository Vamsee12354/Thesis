from unittest import TestCase
from implementation_manual import IsValidPassword

class TestIsValidPassword(TestCase):
    def test_missing_password(self):
        self.assertEqual(IsValidPassword(""), ["Please fill the password"])

    def test_weak_password_short(self):
        self.assertEqual(IsValidPassword("short"), ["Length must be between 12 and 72 characters", "Password must contain an uppercase letter", "Password must contain a special character or a number"])

    def test_weak_password_missing_lowercase(self):
        self.assertEqual(IsValidPassword("UPPERCASE1!"), ["Password must contain a lowercase letter"])

    def test_weak_password_missing_uppercase(self):
        self.assertEqual(IsValidPassword("lowercase1!"), ["Password must contain an uppercase letter"])

    def test_weak_password_missing_special_or_number(self):
        self.assertEqual(IsValidPassword("lowercaseUppercase"), ["Password must contain a special character or a number"])

    def test_strong_password(self):
        self.assertEqual(IsValidPassword("Lowercase1!"), "The password is valid")

    def test_password_too_long(self):
        self.assertEqual(IsValidPassword("a" * 73), ["Length must be between 12 and 72 characters"])

    def test_password_with_all_requirements(self):
        self.assertEqual(IsValidPassword("ValidPassword1!"), "The password is valid")