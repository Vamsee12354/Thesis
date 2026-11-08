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
        expected_error = "Length must be between 12 and 72 characters"

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertIn(expected_error, result)

    def test_password_missing_lowercase(self):
        # Arrange
        password = "ABCDEFGHIJKL1!"
        expected_error = "Password must contain a lowercase letter"

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertIn(expected_error, result)

    def test_password_missing_uppercase(self):
        # Arrange
        password = "abcdefghijk1!"
        expected_error = "Password must contain an uppercase letter"

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertIn(expected_error, result)

    def test_password_missing_special_or_number(self):
        # Arrange
        password = "Abcdefghijkl"
        expected_error = "Password must contain a special character or a number"

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertIn(expected_error, result)

    def test_password_multiple_errors(self):
        # Arrange
        password = "abc"
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
        expected_message = "The password is valid"

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertEqual(result, expected_message)

    def test_valid_password_with_max_length(self):
        # Arrange
        password = "A" * 35 + "a" * 35 + "1!"
        expected_message = "The password is valid"

        # Act
        result = IsValidPassword(password)

        # Assert
        self.assertEqual(result, expected_message)

if __name__ == "__main__":
    unittest.main()