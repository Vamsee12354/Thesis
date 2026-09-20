import unittest
from implementation_manual import validate_form

class TestFormValidation(unittest.TestCase):

    def test_valid_form(self):
        result = validate_form("John", "Marston", "john@example.com", "Frage", "Hallo!", True)
        self.assertEqual(result, "Form is valid. Details:John,Marston,john@example.com,Frage,Hallo!,True")

    def test_missing_privacy(self):
        result = validate_form("Alex", "John", "abc@gmail.net", "Question", "Hallo!", False)
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_empty_form(self):
        result = validate_form("", "", "", "", "", "")
        self.assertEqual(result, ['Please Type First Name', 'Please Type Last Name', 'Please Type EmailID', 'Please Type Subject', 'Please Type Message', 'Please confirm the privacy policy'])

    def test_invalid_email(self):
        result = validate_form("John", "Doe", "invalid_email", "Question", "Hello", True)
        self.assertEqual(result, ["Email standards not followed", "Please confirm the privacy policy"])

    def test_blank_email(self):
        result = validate_form("John", "Doe", "   ", "Question", "Hello", True)
        self.assertEqual(result, ["Please Type EmailID", "Please confirm the privacy policy"])

    def test_missing_fields(self):
        result = validate_form("John", "", "john@example.com", "", "Hello", True)
        self.assertEqual(result, ["Please Type Last Name", "Please Type Subject", "Please Type Message", "Please confirm the privacy policy"])

    def test_only_whitespace_fields(self):
        result = validate_form("   ", "   ", "   ", "   ", "   ", "   ")
        self.assertEqual(result, ['Please Type First Name', 'Please Type Last Name', 'Please Type EmailID', 'Please Type Subject', 'Please Type Message', 'Please confirm the privacy policy'])

if __name__ == '__main__':
    unittest.main()
