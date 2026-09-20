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
        result = validate_form("John", "Doe", "invalid_email", "Question", "Hello!", True)
        self.assertEqual(result, ['Email standards not followed'])

    def test_missing_email(self):
        result = validate_form("John", "Doe", "", "Question", "Hello!", True)
        self.assertEqual(result, ['Please Type EmailID'])

    def test_missing_subject(self):
        result = validate_form("John", "Doe", "john@example.com", "", "Hello!", True)
        self.assertEqual(result, ['Please Type Subject'])

    def test_missing_message(self):
        result = validate_form("John", "Doe", "john@example.com", "Question", "", True)
        self.assertEqual(result, ['Please Type Message'])

    def test_missing_first_name(self):
        result = validate_form("", "Doe", "john@example.com", "Question", "Hello!", True)
        self.assertEqual(result, ['Please Type First Name'])

    def test_missing_last_name(self):
        result = validate_form("John", "", "john@example.com", "Question", "Hello!", True)
        self.assertEqual(result, ['Please Type Last Name'])

    def test_multiple_errors(self):
        result = validate_form("", "", "invalid_email", "", "Hello!", False)
        self.assertEqual(result, ['Please Type First Name', 'Please Type Last Name', 'Email standards not followed', 'Please Type Subject', 'Please confirm the privacy policy'])

if __name__ == '__main__':
    unittest.main()
