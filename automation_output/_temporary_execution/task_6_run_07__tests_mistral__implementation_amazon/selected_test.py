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
        long_password = "a" * 73
        result = IsValidPassword(long_password)
        self.assertEqual(result, ["Length must be between 12 and 72 characters"])

    def test_password_exactly_12_chars(self):
        result = IsValidPassword("Aa1!Aa1!Aa1!A")
        self.assertEqual(result, "The password is valid")

    def test_password_exactly_72_chars(self):
        result = IsValidPassword("Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!")
        self.assertEqual(result, "The password is valid")

    def test_missing_lowercase(self):
        result = IsValidPassword("ALLUPPERCASE123!")
        self.assertEqual(result, ["Password must contain a lowercase letter"])

    def test_missing_uppercase(self):
        result = IsValidPassword("alllowercase123!")
        self.assertEqual(result, ["Password must contain an uppercase letter"])

    def test_missing_special_or_number(self):
        result = IsValidPassword("AllUppercaseLowercase")
        self.assertEqual(result, ["Password must contain a special character or a number"])

    def test_missing_multiple_requirements(self):
        result = IsValidPassword("short")
        self.assertEqual(result, [
            "Length must be between 12 and 72 characters",
            "Password must contain an uppercase letter",
            "Password must contain a special character or a number"
        ])

    def test_valid_password_with_all_requirements(self):
        result = IsValidPassword("ValidPass123!")
        self.assertEqual(result, "The password is valid")

    def test_valid_password_with_special_chars(self):
        result = IsValidPassword("Another@Valid1")
        self.assertEqual(result, "The password is valid")

    def test_password_with_spaces(self):
        result = IsValidPassword(" Valid Pass123! ")
        self.assertEqual(result, "The password is valid")

    def test_password_with_only_special_chars(self):
        result = IsValidPassword("!@#$%^&*()_+")
        self.assertEqual(result, [
            "Length must be between 12 and 72 characters",
            "Password must contain a lowercase letter",
            "Password must contain an uppercase letter"
        ])