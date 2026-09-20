from implementation_manual import IsValidPassword
import unittest

class TestIsValidPassword(unittest.TestCase):

    def test_missing_password(self):
        result = IsValidPassword("")
        self.assertEqual(result, ["Please fill the password"])

    def test_password_none(self):
        result = IsValidPassword(None)
        self.assertEqual(result, ["Please fill the password"])

    def test_password_too_short(self):
        result = IsValidPassword("short")
        self.assertEqual(result, ["Length must be between 12 and 72 characters"])

    def test_password_too_long(self):
        result = IsValidPassword("a" * 73)
        self.assertEqual(result, ["Length must be between 12 and 72 characters"])

    def test_password_exact_min_length(self):
        result = IsValidPassword("Aa1!aaaaaaaaa")
        self.assertEqual(result, "The password is valid")

    def test_password_exact_max_length(self):
        result = IsValidPassword("Aa1!aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        self.assertEqual(result, "The password is valid")

    def test_password_missing_lowercase(self):
        result = IsValidPassword("AAAAAAAAAAAA1!")
        self.assertEqual(result, ["Password must contain a lowercase letter"])

    def test_password_missing_uppercase(self):
        result = IsValidPassword("aaaaaaaaaaaa1!")
        self.assertEqual(result, ["Password must contain an uppercase letter"])

    def test_password_missing_special_or_number(self):
        result = IsValidPassword("Aaaaaaaaaaaaaa")
        self.assertEqual(result, ["Password must contain a special character or a number"])

    def test_password_missing_multiple_requirements(self):
        result = IsValidPassword("short")
        self.assertEqual(result, [
            "Length must be between 12 and 72 characters",
            "Password must contain an uppercase letter",
            "Password must contain a special character or a number"
        ])

    def test_password_missing_all_requirements(self):
        result = IsValidPassword("12345")
        self.assertEqual(result, [
            "Length must be between 12 and 72 characters",
            "Password must contain an uppercase letter",
            "Password must contain a lowercase letter",
            "Password must contain a special character or a number"
        ])

    def test_valid_password_with_all_requirements(self):
        result = IsValidPassword("ValidPass123!")
        self.assertEqual(result, "The password is valid")

    def test_valid_password_with_special_chars(self):
        result = IsValidPassword("Valid_Pass@123")
        self.assertEqual(result, "The password is valid")

    def test_password_with_spaces(self):
        result = IsValidPassword(" Valid Pass123! ")
        self.assertEqual(result, "The password is valid")

    def test_password_with_only_special_chars(self):
        result = IsValidPassword("!@#$%^&*()_+")
        self.assertEqual(result, [
            "Length must be between 12 and 72 characters",
            "Password must contain an uppercase letter",
            "Password must contain a lowercase letter"
        ])