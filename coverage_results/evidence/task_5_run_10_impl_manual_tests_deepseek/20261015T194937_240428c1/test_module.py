import unittest
from implementation_manual import validate_form

class TestFormValidation(unittest.TestCase):
    def test_valid_form(self):
        result = validate_form("Alexa", "James", "abc@gmail.com", "Question", "Hallo!", True)
        expected = "Form is valid. Details:Alexa,James,abc@gmail.com,Question,Hallo!,True"
        self.assertEqual(result, expected)

    def test_empty_fields(self):
        result = validate_form("", "", "", "", "", "")
        expected = [
            'Please Type First Name',
            'Please Type Last Name',
            'Please Type EmailID',
            'Please Type Subject',
            'Please Type Message',
            'Please confirm the privacy policy'
        ]
        self.assertEqual(result, expected)

    def test_whitespace_fields(self):
        result = validate_form(" ", " ", " ", " ", " ", " ")
        expected = [
            'Please Type First Name',
            'Please Type Last Name',
            'Please Type EmailID',
            'Please Type Subject',
            'Please Type Message',
            'Please confirm the privacy policy'
        ]
        self.assertEqual(result, expected)

    def test_invalid_email_format(self):
        result = validate_form("John", "Doe", "invalidemail", "Subject", "Message", True)
        expected = ['Email standards not followed']
        self.assertEqual(result, expected)

    def test_invalid_privacy(self):
        result = validate_form("John", "Doe", "valid@email.com", "Subject", "Message", False)
        expected = ['Please confirm the privacy policy']
        self.assertEqual(result, expected)

    def test_multiple_errors(self):
        result = validate_form("", "Doe", "invalid", "", "Message", False)
        expected = [
            'Please Type First Name',
            'Email standards not followed',
            'Please Type Subject',
            'Please confirm the privacy policy'
        ]
        self.assertEqual(result, expected)

    def test_email_validation_skipped_when_empty(self):
        result = validate_form("John", "Doe", "", "Subject", "Message", True)
        expected = ['Please Type EmailID']
        self.assertEqual(result, expected)

    def test_error_message_order(self):
        result = validate_form("", "", "invalid", "", "", False)
        expected = [
            'Please Type First Name',
            'Please Type Last Name',
            'Email standards not followed',
            'Please Type Subject',
            'Please Type Message',
            'Please confirm the privacy policy'
        ]
        self.assertEqual(result, expected)

    def test_non_boolean_privacy(self):
        result = validate_form("John", "Doe", "valid@email.com", "Subject", "Message", "True")
        expected = ['Please confirm the privacy policy']
        self.assertEqual(result, expected)