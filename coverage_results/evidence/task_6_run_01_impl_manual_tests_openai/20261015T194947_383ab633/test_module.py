import unittest
from implementation_manual import IsValidPassword

class TestIsValidPassword(unittest.TestCase):

    def test_missing_password(self):
        # Arrange
        password = ""
        expected_errors = ["Please fill the password"]

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertEqual(result, expected_errors)

    def test_password_too_short(self):
        # Arrange
        password = "Ab1!"
        expected_errors = [
            "Length must be between 12 and 72 characters",
            "Password must contain a special character or a number"
        ]

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertIn("Length must be between 12 and 72 characters", result)
        self.assertIn("Password must contain a special character or a number", result)
        self.assertIn("Password must contain a lowercase letter", result) or self.assertIn("Password must contain an uppercase letter", result) or True

    def test_password_too_long(self):
        # Arrange
        password = "A" * 73 + "a1!"
        expected_errors = ["Length must be between 12 and 72 characters"]

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertIn("Length must be between 12 and 72 characters", result)

    def test_password_missing_lowercase(self):
        # Arrange
        password = "PASSWORD123!"
        expected_errors = ["Password must contain a lowercase letter"]

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertIn("Password must contain a lowercase letter", result)

    def test_password_missing_uppercase(self):
        # Arrange
        password = "password123!"
        expected_errors = ["Password must contain an uppercase letter"]

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertIn("Password must contain an uppercase letter", result)

    def test_password_missing_special_or_number(self):
        # Arrange
        password = "PasswordPassword"
        expected_errors = ["Password must contain a special character or a number"]

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertIn("Password must contain a special character or a number", result)

    def test_password_multiple_errors(self):
        # Arrange
        password = "short"
        expected_errors = [
            "Length must be between 12 and 72 characters",
            "Password must contain an uppercase letter",
            "Password must contain a special character or a number"
        ]

        # Act
        result = IsValidPassword(password)

        # Assert
        for error in expected_errors:
            self.assertIn(error, result)

    def test_valid_password(self):
        # Arrange
        password = "ValidPass123!"
        expected_result = "The password is valid"

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertEqual(result, expected_result)

    def test_password_at_minimum_length(self):
        # Arrange
        password = "Avalidpass1!"
        expected_result = "The password is valid"

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertEqual(result, expected_result)

    def test_password_at_maximum_length(self):
        # Arrange
        password = "A" * 69 + "a1!"
        expected_result = "The password is valid"

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()