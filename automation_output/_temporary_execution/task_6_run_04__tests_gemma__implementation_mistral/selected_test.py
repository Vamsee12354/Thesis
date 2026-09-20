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

    def test_missing_password_returns_fill_error(self):
        # Arrange
        password = ""
        expected = ["Please fill the password"]

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertEqual(result, expected)

    def test_none_password_returns_fill_error(self):
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

    def test_missing_special_or_number_returns_error(self):
        # Arrange
        password = "StrongPassword"
        expected = ["Password must contain a special character or a number"]

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertEqual(result, expected)

    def test_multiple_validation_failures(self):
        # Arrange
        # Short, no uppercase, no special/number
        password = "abc"
        expected = [
            "Length must be between 12 and 72 characters",
            "Password must contain an uppercase letter",
            "Password must contain a special character or a number"
        ]

        # Act
        result = IsValidPassword(password)

        # Assert
        # We check if all expected errors are present since order might vary depending on implementation
        for error in expected:
            self.assertIn(error, result)
        self.assertEqual(len(result), len(expected))

    def test_boundary_length_12_is_valid(self):
        # Arrange
        password = "Abcdefghij1!"
        expected = "The password is valid"

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertEqual(result, expected)

    def test_boundary_length_72_is_valid(self):
        # Arrange
        password = "A" * 70 + "a1!"
        expected = "The password is valid"

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()