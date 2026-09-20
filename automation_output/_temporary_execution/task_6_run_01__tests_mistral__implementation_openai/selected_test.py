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

    def test_password_missing_lowercase(self):
        result = IsValidPassword("ALLUPPERCASE123!")
        self.assertEqual(result, ["Password must contain a lowercase letter"])

    def test_password_missing_uppercase(self):
        result = IsValidPassword("alllowercase123!")
        self.assertEqual(result, ["Password must contain an uppercase letter"])

    def test_password_missing_special_or_number(self):
        result = IsValidPassword("AllLowercaseLetters")
        self.assertEqual(result, ["Password must contain a special character or a number"])

    def test_password_missing_multiple_requirements(self):
        result = IsValidPassword("short")
        expected = [
            "Length must be between 12 and 72 characters",
            "Password must contain an uppercase letter",
            "Password must contain a special character or a number"
        ]
        self.assertEqual(result, expected)

    def test_password_meets_all_requirements(self):
        result = IsValidPassword("ValidPass123!")
        self.assertEqual(result, "The password is valid")

    def test_password_with_all_special_characters(self):
        result = IsValidPassword("ValidPass123!?@#$%^&*_")
        self.assertEqual(result, "The password is valid")

    def test_password_with_numbers_only(self):
        result = IsValidPassword("ValidPass1234567890")
        self.assertEqual(result, "The password is valid")

    def test_password_with_minimum_length(self):
        result = IsValidPassword("Aa1!Aa1!Aa1!Aa")
        self.assertEqual(result, "The password is valid")

    def test_password_with_maximum_length(self):
        result = IsValidPassword("Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!")
        self.assertEqual(result, "The password is valid")

    def test_password_with_spaces(self):
        result = IsValidPassword("Valid Pass 123!")
        self.assertEqual(result, "The password is valid")