import unittest
from implementation_manual import validate_form

class TestFormValidation(unittest.TestCase):
    def test_valid_form(self):
        result = validate_form("Alexa", "James", "abc@gmail.com", "Question", "Hallo!", True)
        self.assertEqual(result, "Form is valid. Details:Alexa,James,abc@gmail.com,Question,Hallo!,True")

    def test_invalid_privacy(self):
        result = validate_form("Alex", "John", "abc@gmail.net", "Question", "Hallo!", False)
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_empty_fields(self):
        result = validate_form("", "", "", "", "", "")
        self.assertEqual(result, ['Please Type First Name', 'Please Type Last Name', 'Please Type EmailID', 'Please Type Subject', 'Please Type Message', 'Please confirm the privacy policy'])

    def test_whitespace_fields(self):
        result = validate_form(" ", " ", " ", " ", " ", "")
        self.assertEqual(result, ['Please Type First Name', 'Please Type Last Name', 'Please Type EmailID', 'Please Type Subject', 'Please Type Message', 'Please confirm the privacy policy'])

    def test_invalid_email_format(self):
        result = validate_form("John", "Doe", "invalid-email", "Subject", "Message", True)
        self.assertEqual(result, ["Email standards not followed"])

    def test_multiple_errors(self):
        result = validate_form("", "Doe", "invalid-email", "", "Message", False)
        self.assertEqual(result, ['Please Type First Name', 'Email standards not followed', 'Please Type Subject', 'Please confirm the privacy policy'])

    def test_valid_form_with_whitespace(self):
        result = validate_form(" John ", " Doe ", " john@example.com ", " Subject ", " Message ", True)
        self.assertEqual(result, "Form is valid. Details:John,Doe,john@example.com,Subject,Message,True")

    def test_invalid_privacy_type(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "True")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_email_empty(self):
        result = validate_form("John", "Doe", "", "Subject", "Message", True)
        self.assertEqual(result, ["Please Type EmailID"])

    def test_invalid_email_whitespace(self):
        result = validate_form("John", "Doe", " ", "Subject", "Message", True)
        self.assertEqual(result, ["Please Type EmailID"])

    def test_invalid_subject_empty(self):
        result = validate_form("John", "Doe", "john@example.com", "", "Message", True)
        self.assertEqual(result, ["Please Type Subject"])

    def test_invalid_message_empty(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "", True)
        self.assertEqual(result, ["Please Type Message"])

    def test_invalid_first_name_empty(self):
        result = validate_form("", "Doe", "john@example.com", "Subject", "Message", True)
        self.assertEqual(result, ["Please Type First Name"])

    def test_invalid_last_name_empty(self):
        result = validate_form("John", "", "john@example.com", "Subject", "Message", True)
        self.assertEqual(result, ["Please Type Last Name"])

    def test_invalid_privacy_empty(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_false(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", False)
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_multiple_invalid_fields(self):
        result = validate_form("", "", "invalid-email", "", "", False)
        self.assertEqual(result, ['Please Type First Name', 'Please Type Last Name', 'Email standards not followed', 'Please Type Subject', 'Please Type Message', 'Please confirm the privacy policy'])