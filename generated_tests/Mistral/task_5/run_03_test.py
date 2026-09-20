from implementation_manual import validate_form
import unittest

class TestValidateForm(unittest.TestCase):

    def test_valid_form(self):
        result = validate_form("Alexa", "James", "abc@gmail.com", "Question", "Hallo!", True)
        self.assertEqual(result, "Form is valid. Details:Alexa,James,abc@gmail.com,Question,Hallo!,True")

    def test_empty_fields(self):
        result = validate_form("", "", "", "", "", "")
        expected_errors = [
            "Please Type First Name",
            "Please Type Last Name",
            "Please Type EmailID",
            "Please Type Subject",
            "Please Type Message",
            "Please confirm the privacy policy"
        ]
        self.assertEqual(result, expected_errors)

    def test_whitespace_only_fields(self):
        result = validate_form("   ", "   ", "   ", "   ", "   ", False)
        expected_errors = [
            "Please Type First Name",
            "Please Type Last Name",
            "Please Type EmailID",
            "Please Type Subject",
            "Please Type Message",
            "Please confirm the privacy policy"
        ]
        self.assertEqual(result, expected_errors)

    def test_missing_first_name(self):
        result = validate_form("", "Doe", "john@example.com", "Hi", "Hello", True)
        expected_errors = ["Please Type First Name"]
        self.assertEqual(result, expected_errors)

    def test_missing_last_name(self):
        result = validate_form("John", "", "john@example.com", "Hi", "Hello", True)
        expected_errors = ["Please Type Last Name"]
        self.assertEqual(result, expected_errors)

    def test_missing_email(self):
        result = validate_form("John", "Doe", "", "Hi", "Hello", True)
        expected_errors = ["Please Type EmailID"]
        self.assertEqual(result, expected_errors)

    def test_invalid_email_format(self):
        result = validate_form("John", "Doe", "invalid-email", "Hi", "Hello", True)
        expected_errors = ["Email standards not followed"]
        self.assertEqual(result, expected_errors)

    def test_missing_subject(self):
        result = validate_form("John", "Doe", "john@example.com", "", "Hello", True)
        expected_errors = ["Please Type Subject"]
        self.assertEqual(result, expected_errors)

    def test_missing_message(self):
        result = validate_form("John", "Doe", "john@example.com", "Hi", "", True)
        expected_errors = ["Please Type Message"]
        self.assertEqual(result, expected_errors)

    def test_missing_privacy(self):
        result = validate_form("John", "Doe", "john@example.com", "Hi", "Hello", False)
        expected_errors = ["Please confirm the privacy policy"]
        self.assertEqual(result, expected_errors)

    def test_multiple_errors(self):
        result = validate_form("", "Doe", "invalid-email", "", "Hello", False)
        expected_errors = [
            "Please Type First Name",
            "Please Type EmailID",
            "Email standards not followed",
            "Please Type Subject",
            "Please confirm the privacy policy"
        ]
        self.assertEqual(result, expected_errors)

    def test_email_with_whitespace(self):
        result = validate_form("John", "Doe", "  john@example.com  ", "Hi", "Hello", True)
        expected = "Form is valid. Details:John,Doe,john@example.com,Hi,Hello,True"
        self.assertEqual(result, expected)

    def test_privacy_not_boolean(self):
        result = validate_form("John", "Doe", "john@example.com", "Hi", "Hello", "True")
        expected_errors = ["Please confirm the privacy policy"]
        self.assertEqual(result, expected_errors)

    def test_privacy_none(self):
        result = validate_form("John", "Doe", "john@example.com", "Hi", "Hello", None)
        expected_errors = ["Please confirm the privacy policy"]
        self.assertEqual(result, expected_errors)