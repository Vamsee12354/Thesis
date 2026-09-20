from unittest import TestCase
from implementation_manual import IsValidPassword

class TestIsValidPassword(TestCase):
    def test_missing_password(self):
        self.assertEqual(IsValidPassword(""), ["Please fill the password"])

    def test_weak_password_short(self):
        self.assertEqual(IsValidPassword("short"), ["Length must be between 12 and 72 characters", "Password must contain an uppercase letter", "Password must contain a special character or a number"])

    def test_weak_password_no_uppercase(self):
        self.assertEqual(IsValidPassword("nouppercase1!"), ["Password must contain an uppercase letter"])

    def test_weak_password_no_special_or_number(self):
        self.assertEqual(IsValidPassword("nospecialornumber"), ["Password must contain a special character or a number"])

    def test_weak_password_all_issues(self):
        self.assertEqual(IsValidPassword("weak"), ["Length must be between 12 and 72 characters", "Password must contain an uppercase letter", "Password must contain a special character or a number"])

    def test_strong_password(self):
        self.assertEqual(IsValidPassword("StrongPass1!"), "The password is valid")

    def test_password_too_long(self):
        self.assertEqual(IsValidPassword("a" * 73), ["Length must be between 12 and 72 characters"])

    def test_password_with_all_required_characters(self):
        self.assertEqual(IsValidPassword("ValidPassword1!"), "The password is valid")