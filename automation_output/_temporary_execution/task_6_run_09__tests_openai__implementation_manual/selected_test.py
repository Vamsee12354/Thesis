import unittest
from implementation_manual import IsValidPassword

class TestIsValidPassword(unittest.TestCase):

    def test_missing_password(self):
        # Arrange
        password = ""
        # Act
        result = IsValidPassword(password)
        # Assert
        self.assertEqual(result, ["Please fill the password"])

    def test_password_too_short(self):
        # Arrange
        password = "Ab1!"
        # Act
        result = IsValidPassword(password)
        # Assert
        self.assertIn("Length must be between 12 and 72 characters", result)

    def test_password_too_long(self):
        # Arrange
        password = "A" * 73 + "b1!"
        # Act
        result = IsValidPassword(password)
        # Assert
        self.assertIn("Length must be between 12 and 72 characters", result)

    def test_password_missing_lowercase(self):
        # Arrange
        password = "ABCDEFGHIJKL1!"
        # Act
        result = IsValidPassword(password)
        # Assert
        self.assertIn("Password must contain a lowercase letter", result)

    def test_password_missing_uppercase(self):
        # Arrange
        password = "abcdefghijk1!"
        # Act
        result = IsValidPassword(password)
        # Assert
        self.assertIn("Password must contain an uppercase letter", result)

    def test_password_missing_special_or_number(self):
        # Arrange
        password = "Abcdefghijkl"
        # Act
        result = IsValidPassword(password)
        # Assert
        self.assertIn("Password must contain a special character or a number", result)

    def test_password_multiple_errors(self):
        # Arrange
        password = "abc"
        # Act
        result = IsValidPassword(password)
        # Assert
        self.assertIn("Length must be between 12 and 72 characters", result)
        self.assertIn("Password must contain an uppercase letter", result)
        self.assertIn("Password must contain a special character or a number", result)

    def test_valid_password(self):
        # Arrange
        password = "Abcdefghijk1!"
        # Act
        result = IsValidPassword(password)
        # Assert
        self.assertEqual(result, "The password is valid")

    def test_password_exact_min_length(self):
        # Arrange
        password = "A1bcdefghijk"
        # Act
        result = IsValidPassword(password)
        # Assert
        self.assertEqual(result, "The password is valid")

    def test_password_exact_max_length(self):
        # Arrange
        password = "A1" + "b" * 69 + "!"
        # Act
        result = IsValidPassword(password)
        # Assert
        self.assertEqual(result, "The password is valid")

    def test_password_with_only_required_characters(self):
        # Arrange
        password = "aA1" + "b" * 9
        # Act
        result = IsValidPassword(password)
        # Assert
        self.assertEqual(result, "The password is valid")

if __name__ == "__main__":
    unittest.main()