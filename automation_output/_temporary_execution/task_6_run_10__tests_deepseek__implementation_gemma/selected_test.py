from implementation_manual import IsValidPassword
import unittest


class TestIsValidPassword(unittest.TestCase):
    def test_missing_password(self):
        self.assertEqual(IsValidPassword(""), ["Please fill the password"])

    def test_password_too_short(self):
        self.assertEqual(
            IsValidPassword("Short1!"),
            ["Length must be between 12 and 72 characters"],
        )

    def test_password_too_long(self):
        self.assertEqual(
            IsValidPassword("A" * 73 + "a1!"),
            ["Length must be between 12 and 72 characters"],
        )

    def test_missing_lowercase(self):
        self.assertEqual(
            IsValidPassword("UPPERCASE123!"),
            ["Password must contain a lowercase letter"],
        )

    def test_missing_uppercase(self):
        self.assertEqual(
            IsValidPassword("lowercase123!"),
            ["Password must contain an uppercase letter"],
        )

    def test_missing_special_or_number(self):
        self.assertEqual(
            IsValidPassword("MixedCaseLetters"),
            ["Password must contain a special character or a number"],
        )

    def test_multiple_errors(self):
        self.assertEqual(
            IsValidPassword("short"),
            [
                "Length must be between 12 and 72 characters",
                "Password must contain an uppercase letter",
                "Password must contain a special character or a number",
            ],
        )

    def test_valid_password(self):
        self.assertEqual(IsValidPassword("ValidPassword123!"), "The password is valid")

    def test_valid_password_with_special_chars(self):
        self.assertEqual(IsValidPassword("AnotherValid!@#1"), "The password is valid")

    def test_valid_password_max_length(self):
        self.assertEqual(
            IsValidPassword("A" * 60 + "a" * 10 + "1!"), "The password is valid"
        )