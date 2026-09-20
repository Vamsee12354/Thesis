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

    def test_privacy_not_boolean(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "True")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_valid_form_with_whitespace(self):
        result = validate_form(" John ", " Doe ", " john@example.com ", " Subject ", " Message ", True)
        self.assertEqual(result, "Form is valid. Details:John,Doe,john@example.com,Subject,Message,True")

    def test_empty_email(self):
        result = validate_form("John", "Doe", "", "Subject", "Message", True)
        self.assertEqual(result, ["Please Type EmailID"])

    def test_invalid_email_and_privacy(self):
        result = validate_form("John", "Doe", "invalid-email", "Subject", "Message", False)
        self.assertEqual(result, ["Email standards not followed", "Please confirm the privacy policy"])