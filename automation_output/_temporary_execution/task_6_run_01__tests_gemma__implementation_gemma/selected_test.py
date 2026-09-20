import unittest
from implementation_manual import IsValidPassword

class TestIsValidPassword(unittest.TestCase):

    def test_valid_password_returns_success_message(self):
        # Arrange
        password = "StrongPassword123!"
        expected = "The password is valid"

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertEqual(result, expected)

    def test_missing_password_returns_error(self):
        # Arrange
        password = ""
        expected = ["Please fill the password"]

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertEqual(result, expected)

    def test_none_password_returns_error(self):
        # Arrange
        password = None
        expected = ["Please fill the password"]

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertEqual(result, expected)

    def test_password_too_short_returns_length_error(self):
        # Arrange
        password = "Ab1!"
        expected = ["Length must be between 12 and 72 characters"]

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertEqual(result, expected)

    def test_password_too_long_returns_length_error(self):
        # Arrange
        password = "A" * 73 + "a1!"
        expected = ["Length must be between 12 and 72 characters"]

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertEqual(result, expected)

    def test_missing_lowercase_returns_error(self):
        # Arrange
        password = "STRONGPASS123!"
        expected = ["Password must contain a lowercase letter"]

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertEqual(result, expected)

    def test_missing_uppercase_returns_error(self):
        # Arrange
        password = "strongpass123!"
        expected = ["Password must contain an uppercase letter"]

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertEqual(result, expected)

    def test_missing_special