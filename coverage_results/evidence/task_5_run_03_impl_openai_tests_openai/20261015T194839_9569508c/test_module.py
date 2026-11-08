import unittest
from implementation_manual import validate_form

class TestValidateForm(unittest.TestCase):

    def test_valid_form(self):
        # Arrange
        first_name = "Alexa"
        last_name = "James"
        email = "abc@gmail.com"
        subject = "Question"
        message = "Hallo!"
        privacy = True
        expected = "Form is valid. Details:Alexa,James,abc@gmail.com,Question,Hallo!,True"
        # Act
        result = validate_form(first_name, last_name, email, subject, message, privacy)
        # Assert
        self.assertEqual(result, expected)

    def test_privacy_policy_not_confirmed(self):
        # Arrange
        first_name = "Alex"
        last_name = "John"
        email = "abc@gmail.net"
        subject = "Question"
        message = "Hallo!"
        privacy = False
        expected = ["Please confirm the privacy policy"]
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
        privacy = ""
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

    def test_fields_with_whitespace_only(self):
        # Arrange
        first_name = "   "
        last_name = "  "
        email = "   "
        subject = " "
        message = "    "
        privacy = True
        expected = [
            'Please Type First Name',
            'Please Type Last Name',
            'Please Type EmailID',
            'Please Type Subject',
            'Please Type Message'
        ]
        # Act
        result = validate_form(first_name, last_name, email, subject, message, privacy)
        # Assert
        self.assertEqual(result, expected)

    def test_invalid_email_format(self):
        # Arrange
        first_name = "John"
        last_name = "Doe"
        email = "john.doe@invalid-email"
        subject = "Hello"
        message = "Test message"
        privacy = True
        expected = ["Email standards not followed"]
        # Act
        result = validate_form(first_name, last_name, email, subject, message, privacy)
        # Assert
        self.assertEqual(result, expected)

    def test_email_empty_and_other_errors(self):
        # Arrange
        first_name = " "
        last_name = " "
        email = " "
        subject = " "
        message = " "
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

    def test_multiple_errors_including_invalid_email(self):
        # Arrange
        first_name = "John"
        last_name = ""
        email = "invalid-email@"
        subject = ""
        message = " "
        privacy = False
        expected = [
            'Please Type Last Name',
            'Email standards not followed',
            'Please Type Subject',
            'Please Type Message',
            'Please confirm the privacy policy'
        ]
        # Act
        result = validate_form(first_name, last_name, email, subject, message, privacy)
        # Assert
        self.assertEqual(result, expected)

    def test_privacy_not_boolean(self):
        # Arrange
        first_name = "John"
        last_name = "Doe"
        email = "john@example.com"
        subject = "Subject"
        message = "Message"
        privacy = "yes"
        expected = ["Please confirm the privacy policy"]
        # Act
        result = validate_form(first_name, last_name, email, subject, message, privacy)
        # Assert
        self.assertEqual(result, expected)

    def test_email_with_leading_trailing_spaces(self):
        # Arrange
        first_name = "John"
        last_name = "Doe"
        email = "  john@example.com  "
        subject = "Subject"
        message = "Message"
        privacy = True
        expected = "Form is valid. Details:John,Doe,john@example.com,Subject,Message,True"
        # Act
        result = validate_form(first_name, last_name, email, subject, message, privacy)
        # Assert
        self.assertEqual(result, expected)

    def test_order_of_error_messages(self):
        # Arrange
        first_name = ""
        last_name = ""
        email = "invalid-email"
        subject = ""
        message = ""
        privacy = False
        expected = [
            'Please Type First Name',
            'Please Type Last Name',
            'Email standards not followed',
            'Please Type Subject',
            'Please Type Message',
            'Please confirm the privacy policy'
        ]
        # Act
        result = validate_form(first_name, last_name, email, subject, message, privacy)
        # Assert
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()