from unittest import TestCase
from implementation_manual import IsValidPassword

class TestIsValidPassword(TestCase):
    def test_missing_password(self):
        self.assertEqual(IsValidPassword(""), ["Please fill the password"])

    def test_weak_password(self):
        self.assertEqual(IsValidPassword("short"), ["Length must be between 12 and 72 characters", "Password must contain an uppercase letter", "Password must contain a special character or a number"])

    def test_strong_password(self):
        self.assertEqual(IsValidPassword("StrongP@ssw0rd"), "The password is valid")

    def test_password_too_short(self):
        self.assertEqual(IsValidPassword("Abc1!"), ["Length must be between 12 and 72 characters", "Password must contain an uppercase letter", "Password must contain a special character or a number"])

    def test_password_too_long(self):
        self.assertEqual(IsValidPassword("A" * 73), ["Length must be between 12 and 72 characters"])

    def test_no_lowercase(self):
        self.assertEqual(IsValidPassword("ABC123!"), ["Password must contain a lowercase letter"])

    def test_no_uppercase(self):
        self.assertEqual(IsValidPassword("abc123!"), ["Password must contain an uppercase letter"])

    def test_no_special_or_number(self):
        self.assertEqual(IsValidPassword("ABCabc"), ["Password must contain a special character or a number"])

    def test_all_conditions_met(self):
        self.assertEqual(IsValidPassword("ValidP@ssw0rd"), "The password is valid")