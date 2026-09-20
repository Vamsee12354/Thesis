import unittest
from implementation_manual import validate_form

class TestFormValidation(unittest.TestCase):

    def test_valid_form(self):
        result = validate_form("Alexa", "James", "abc@gmail.com", "Question", "Hallo!", True)
        self.assertEqual(result, "Form is valid. Details:Alexa,James,abc@gmail.com,Question,Hallo!,True")

    def test_privacy_policy_rejected(self):
        result = validate_form("Alex", "John", "abc@gmail.net", "Question", "Hallo!", False)
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_empty_form(self):
        result = validate_form("", "", "", "", "", "")
        self.assertEqual(result, ['Please Type First Name', 'Please Type Last Name', 'Please Type EmailID', 'Please Type Subject', 'Please Type Message', 'Please confirm the privacy policy'])

    def test_missing_first_name(self):
        result = validate_form(None, "John", "abc@gmail.com", "Question", "Hallo!", True)
        self.assertEqual(result, ['Please Type First Name', 'Please confirm the privacy policy'])

    def test_missing_last_name(self):
        result = validate_form("Alex", None, "abc@gmail.com", "Question", "Hallo!", True)
        self.assertEqual(result, ['Please Type Last Name', 'Please confirm the privacy policy'])

    def test_missing_email(self):
        result = validate_form("Alex", "John", None, "Question", "Hallo!", True)
        self.assertEqual(result, ['Please Type EmailID', 'Please confirm the privacy policy'])

    def test_missing_subject(self):
        result = validate_form("Alex", "John", "abc@gmail.com", None, "Hallo!", True)
        self.assertEqual(result, ['Please Type Subject', 'Please confirm the privacy policy'])

    def test_missing_message(self):
        result = validate_form("Alex", "John", "abc@gmail.com", "Question", None, True)
        self.assertEqual(result, ['Please Type Message', 'Please confirm the privacy policy'])

    def test_invalid_email(self):
        result = validate_form("Alex", "John", "invalid_email", "Question", "Hallo!", True)
        self.assertEqual(result, ['Email standards not followed', 'Please confirm the privacy policy'])

    def test_invalid_email_empty(self):
        result = validate_form("Alex", "John", "", "Question", "Hallo!", True)
        self.assertEqual(result, ['Please Type EmailID', 'Please confirm the privacy policy'])

    def test_whitespace_fields(self):
        result = validate_form("   ", "   ", "   ", "   ", "   ", "   ")
        self.assertEqual(result, ['Please Type First Name', 'Please Type Last Name', 'Please Type EmailID', 'Please Type Subject', 'Please Type Message', 'Please confirm the privacy policy'])

if __name__ == '__main__':
    unittest.main()
