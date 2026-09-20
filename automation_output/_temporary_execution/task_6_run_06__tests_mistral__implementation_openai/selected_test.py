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

    def test_password_no_lowercase(self):
        result = IsValidPassword("ALLUPPERCASE123!")
        self.assertEqual(result, ["Password must contain a lowercase letter"])

    def test_password_no_uppercase(self):
        result = IsValidPassword("alllowercase123!")
        self.assertEqual(result, ["Password must contain an uppercase letter"])

    def test_password_no_special_or_number(self):
        result = IsValidPassword("AllLowercaseUppercase")
        self.assertEqual(result, ["Password must contain a special character or a number"])

    def test_password_missing_multiple_requirements(self):
        result = IsValidPassword("short")
        expected = [
            "Length must be between 12 and 72 characters",
            "Password must contain an uppercase letter",
            "Password must contain a special character or a number",
            "Password must contain a lowercase letter"
        ]
        self.assertEqual(sorted(result), sorted(expected))

    def test_strong_password(self):
        result = IsValidPassword("StrongPass123!")
        self.assertEqual(result, "The password is valid")

    def test_password_with_all_requirements(self):
        result = IsValidPassword("ValidPass123!")
        self.assertEqual(result, "The password is valid")

    def test_password_with_edge_length(self):
        result = IsValidPassword("Aa1!Aa1!Aa1!Aa")
        self.assertEqual(result, "The password is valid")

    def test_password_with_exactly_12_chars(self):
        result = IsValidPassword("Abcdef12345!")
        self.assertEqual(result, "The password is valid")

    def test_password_with_exactly_72_chars(self):
        result = IsValidPassword("Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa")
        self.assertEqual(result, "The password is valid")