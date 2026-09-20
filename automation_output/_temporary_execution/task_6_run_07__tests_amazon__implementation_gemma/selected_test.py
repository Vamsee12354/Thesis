from unittest import TestCase
from implementation_manual import IsValidPassword

class TestIsValidPassword(TestCase):
    def test_missing_password(self):
        self.assertEqual(IsValidPassword(""), ["Please fill the password"])

    def test_weak_password(self):
        self.assertEqual(IsValidPassword("weakpass"), ["Length must be between 12 and 72 characters", "Password must contain an uppercase letter", "Password must contain a special character or a number"])

    def test_strong_password(self):
        self.assertEqual(IsValidPassword("StrongPass1!"), "The password is valid")

    def test_password_too_short(self):
        self.assertEqual(IsValidPassword("Short1!"), ["Length must be between 12 and 72 characters", "Password must contain a special character or a number"])

    def test_password_too_long(self):
        self.assertEqual(IsValidPassword("A" * 73), ["Length must be between 12 and 72 characters"])

    def test_no_lowercase_letter(self):
        self.assertEqual(IsValidPassword("STRONGPASS1!"), ["Password must contain a lowercase letter"])

    def test_no_uppercase_letter(self):
        self.assertEqual(IsValidPassword("strongpass1!"), ["Password must contain an uppercase letter"])

    def test_no_special_character_or_number(self):
        self.assertEqual(IsValidPassword("StrongPassword"), ["Password must contain a special character or a number"])

    def test_empty_string_input(self):
        self.assertEqual(IsValidPassword(" "), ["Length must be between 12 and 72 characters", "Password must contain an uppercase letter", "Password must contain a special character or a number"])

    def test_only_special_characters(self):
        self.assertEqual(IsValidPassword("!@#$%^&*"), ["Length must be between 12 and 72 characters", "Password must contain a lowercase letter", "Password must contain an uppercase letter"])

    def test_only_numbers(self):
        self.assertEqual(IsValidPassword("123456789012"), ["Password must contain a lowercase letter", "Password must contain an uppercase letter", "Password must contain a special character or a number"])

    def test_only_lowercase_letters(self):
        self.assertEqual(IsValidPassword("lowercaseonly"), ["Length must be between 12 and 72 characters", "Password must contain an uppercase letter", "Password must contain a special character or a number"])

    def test_only_uppercase_letters(self):
        self.assertEqual(IsValidPassword("UPPERCASEONLY"), ["Length must be between 12 and 72 characters", "Password must contain a lowercase letter", "Password must contain a special character or a number"])