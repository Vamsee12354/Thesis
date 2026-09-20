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
        self.assertEqual(result, [
            'Please Type First Name',
            'Please Type Last Name',
            'Please Type EmailID',
            'Please Type Subject',
            'Please Type Message',
            'Please confirm the privacy policy'
        ])

    def test_whitespace_fields(self):
        result = validate_form(" ", "  ", "  ", "  ", "  ", " ")
        self.assertEqual(result, [
            'Please Type First Name',
            'Please Type Last Name',
            'Please Type EmailID',
            'Please Type Subject',
            'Please Type Message',
            'Please confirm the privacy policy'
        ])

    def test_invalid_email_format(self):
        result = validate_form("John", "Doe", "invalid-email", "Subject", "Message", True)
        self.assertEqual(result, ["Email standards not followed"])

    def test_missing_first_name(self):
        result = validate_form("", "Doe", "email@test.com", "Subject", "Message", True)
        self.assertEqual(result, ["Please Type First Name"])

    def test_missing_last_name(self):
        result = validate_form("John", "", "email@test.com", "Subject", "Message", True)
        self.assertEqual(result, ["Please Type Last Name"])

    def test_missing_subject(self):
        result = validate_form("John", "Doe", "email@test.com", "", "Message", True)
        self.assertEqual(result, ["Please Type Subject"])

    def test_missing_message(self):
        result = validate_form("John", "Doe", "email@test.com", "Subject", "", True)
        self.assertEqual(result, ["Please Type Message"])

    def test_multiple_errors(self):
        result = validate_form("", "", "bad-email", "", "", False)
        self.assertEqual(result, [
            'Please Type First Name',
            'Please Type Last Name',
            'Email standards not followed',
            'Please Type Subject',
            'Please Type Message',
            'Please confirm the privacy policy'
        ])

    def test_valid_with_whitespace(self):
        result = validate_form(" John ", " Doe ", " email@test.com ", " Subject ", " Message ", True)
        self.assertEqual(result, "Form is valid. Details:John,Doe,email@test.com,Subject,Message,True")

    def test_non_boolean_privacy(self):
        result = validate_form("John", "Doe", "email@test.com", "Subject", "Message", "True")
        self.assertEqual(result, ["Please confirm the privacy policy"])