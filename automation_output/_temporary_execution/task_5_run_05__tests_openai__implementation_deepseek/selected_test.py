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

        # Act
        result = validate_form(first_name, last_name, email, subject, message, privacy)

        # Assert
        expected = "Form is valid. Details:Alexa,James,abc@gmail.com,Question,Hallo!,True"
        self.assertEqual(result, expected)

    def test_privacy_policy_not_confirmed(self):
        # Arrange
        first_name = "Alex"
        last_name = "John"
        email = "abc@gmail.net"
        subject = "Question"
        message = "Hallo!"
        privacy = False

        # Act
        result = validate_form(first_name, last_name, email, subject, message, privacy)

        # Assert
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_all_fields_empty(self):
        # Arrange
        first_name = ""
        last_name = ""
        email = ""
        subject = ""
        message = ""
        privacy = ""

        # Act
        result = validate_form(first_name, last_name, email, subject, message, privacy)

        # Assert
        expected_errors = [
            "Please Type First Name",
            "Please Type Last Name",
            "Please Type EmailID",
            "Please Type Subject",
            "Please Type Message",
            "Please confirm the privacy policy"
        ]
        self.assertEqual(result, expected_errors)

    def test_fields_with_only_whitespace(self):
        # Arrange
        first_name = "   "
        last_name = "  "
        email = "   "
        subject = " "
        message = "    "
        privacy = True

        # Act
        result = validate_form(first_name, last_name, email, subject, message, privacy)

        # Assert
        expected_errors = [
            "Please Type First Name",
            "Please Type Last Name",
            "Please Type EmailID",
            "Please Type Subject",
            "Please Type Message"
        ]
        self.assertEqual(result, expected_errors)

    def test_email_invalid_format(self):
        # Arrange
        first_name = "John"
        last_name = "Doe"
        email = "john.doe@invalid-email"
        subject = "Hello"
        message = "Test message"
        privacy = True

        # Act
        result = validate_form(first_name, last_name, email, subject, message, privacy)

        # Assert
        self.assertEqual(result, ["Email standards not followed"])

    def test_email_empty_and_privacy_false(self):
        # Arrange
        first_name = "John"
        last_name = "Doe"
        email = "   "
        subject = "Hello"
        message = "Test message"
        privacy = False

        # Act
        result = validate_form(first_name, last_name, email, subject, message, privacy)

        # Assert
        expected_errors = [
            "Please Type EmailID",
            "Please confirm the privacy policy"
        ]
        self.assertEqual(result, expected_errors)

    def test_multiple_errors_all_fields_invalid(self):
        # Arrange
        first_name = " "
        last_name = ""
        email = "invalid-email"
        subject = " "
        message = ""
        privacy = False

        # Act
        result = validate_form(first_name, last_name, email, subject, message, privacy)

        # Assert
        expected_errors = [
            "Please Type First Name",
            "Please Type Last Name",
            "Email standards not followed",
            "Please Type Subject",
            "Please Type Message",
            "Please confirm the privacy policy"
        ]
        self.assertEqual(result, expected_errors)

    def test_privacy_not_boolean(self):
        # Arrange
        first_name = "John"
        last_name = "Doe"
        email = "john@example.com"
        subject = "Subject"
        message = "Message"
        privacy = "yes"

        # Act
        result = validate_form(first_name, last_name, email, subject, message, privacy)

        # Assert
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_email_with_leading_trailing_spaces(self):
        # Arrange
        first_name = "John"
        last_name = "Doe"
        email = "  john@example.com  "
        subject = "Subject"
        message = "Message"
        privacy = True

        # Act
        result = validate_form(first_name, last_name, email, subject, message, privacy)

        # Assert
        expected = "Form is valid. Details:John,Doe,john@example.com,Subject,Message,True"
        self.assertEqual(result, expected)

    def test_email_empty_after_trim(self):
        # Arrange
        first_name = "John"
        last_name = "Doe"
        email = "   "
        subject = "Subject"
        message = "Message"
        privacy = True

        # Act
        result = validate_form(first_name, last_name, email, subject, message, privacy)

        # Assert
        self.assertEqual(result, ["Please Type EmailID"])

if __name__ == "__main__":
    unittest.main()