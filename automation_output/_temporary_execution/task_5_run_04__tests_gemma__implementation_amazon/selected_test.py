import unittest
from implementation_manual import validate_form

class TestValidateForm(unittest.TestCase):

    def test_valid_form_submission(self):
        # Arrange
        first_name = "John"
        last_name = "Marston"
        email = "john@example.com"
        subject = "Frage"
        message = "Hallo!"
        privacy = True
        expected = "Form is valid. Details:John,Marston,john@example.com,Frage,Hallo!,True"

        # Act
        result = validate_form(first_name, last_name, email, subject, message, privacy)

        # Assert
        self.assertEqual(result, expected)

    def test_valid_form_with_whitespace_trimming(self):
        # Arrange
        first_name = "  Alexa  "
        last_name = " James "
        email = " abc@gmail.com "
        subject = " Question "
        message = " Hallo! "
        privacy = True
        expected = "Form is valid. Details:Alexa,James,abc@gmail.com,Question,Hallo!,True"

        # Act
        result = validate_form(first_name, last_name, email, subject, message, privacy)

        # Assert
        self.assertEqual(result, expected)

    def test_all_fields_empty(self):
        # Arrange
        first_name = ""
        last_name = ""
        email = ""
        subject = ""
        message = ""
        privacy = False
        expected = [
            'Please Type First Name',
            'Please Type Last Name',
            'Please Type EmailID',
            'Please Type Subject',
            'Please Type Message',
            'Please confirm the privacy policy'
        ]

        # Act
        result = validate_form(first_name, last_name, email, subject, message, privacy)

        # Assert
        self.assertEqual(result, expected)

    def test_missing_first_name(self):
        # Arrange
        result = validate_form(" ", "Doe", "test@test.com", "Sub", "Msg", True)
        expected = ["Please Type First Name"]

        # Act & Assert
        self.assertEqual(result, expected)

    def test_missing_last_name(self):
        # Arrange
        result = validate_form("John", " ", "test@test.com", "Sub", "Msg", True)
        expected = ["Please Type Last Name"]

        # Act & Assert
        self.assertEqual(result, expected)

    def test_missing_email(self):
        # Arrange
        result = validate_form("John", "Doe", "   ", "Sub", "Msg", True)
        expected = ["Please Type EmailID"]

        # Act & Assert
        self.assertEqual(result, expected)

    def test_invalid_email_format(self):
        # Arrange
        result = validate_form("John", "Doe", "invalid-email", "Sub", "Msg", True)
        expected = ["Email standards not followed"]

        # Act & Assert
        self.assertEqual(result, expected)

    def test_missing_subject(self):
        # Arrange
        result = validate_form("John", "Doe", "test@test.com", "", "Msg", True)
        expected = ["Please Type Subject"]

        # Act & Assert
        self.assertEqual(result, expected)

    def test_missing_message(self):
        # Arrange
        result = validate_form("John", "Doe", "test@test.com", "Sub", " ", True)
        expected = ["Please Type Message"]

        # Act & Assert
        self.assertEqual(result, expected)

    def test_privacy_not_confirmed(self):
        # Arrange
        result = validate_form("John", "Doe", "test@test.com", "Sub", "Msg", False)
        expected = ["Please confirm the privacy policy"]

        # Act & Assert
        self.assertEqual(result, expected)

    def test_multiple_errors_order(self):
        # Arrange
        # Missing First Name, Invalid Email, Missing Message, Privacy False
        result = validate_form("", "Doe", "bademail", "Sub", "", False)
        expected = [
            "Please Type First Name",
            "Email standards not followed",
            "Please Type Message",
            "Please confirm the privacy policy"
        ]

        # Act & Assert
        self.assertEqual(result, expected)

    def test_email_regex_edge_cases(self):
        # Arrange
        # Test cases for regex: ~r /^[^\ s@ ]+ @ [^\ s@ ]+\.[^\ s@ ]+ $/
        # Note: The spec regex has spaces around @ in the description, 
        # but standard regex logic and the example imply a standard email check.
        
        # Case: No dot in domain
        res1 = validate_form("A", "B", "a@b", "S", "M", True)
        self.assertIn("Email standards not followed", res1)

        # Case: Multiple @ symbols
        res2 = validate_form("A", "B", "a@b@c.com", "S", "M", True)
        self.assertIn("Email standards not followed", res2)

    def test_privacy_non_boolean(self):
        # Arrange
        # If privacy is not True (e.g., None or a string), it should trigger the error
        result = validate_form("John", "Doe", "test@test.com", "Sub", "Msg", None)
        expected = ["Please confirm the privacy policy"]

        # Act & Assert
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()