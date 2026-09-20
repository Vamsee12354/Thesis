import unittest
from implementation_manual import validate_form

class TestFormValidation(unittest.TestCase):

    def test_valid_form(self):
        result = validate_form("Alexa", "James", "abc@gmail.com", "Question", "Hallo!", True)
        self.assertEqual(result, "Form is valid. Details:Alexa,James,abc@gmail.com,Question,Hallo!,True")

    def test_missing_privacy(self):
        result = validate_form("Alex", "John", "abc@gmail.net", "Question", "Hallo!", False)
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_empty_form(self):
        result = validate_form("", "", "", "", "", "")
        self.assertEqual(result, ['Please Type First Name', 'Please Type Last Name', 'Please Type EmailID', 'Please Type Subject', 'Please Type Message', 'Please confirm the privacy policy'])

    def test_invalid_email(self):
        result = validate_form("Alex", "John", "invalid_email", "Question", "Hallo!", True)
        self.assertEqual(result, ['Email standards not followed'])

    def test_blank_email(self):
        result = validate_form("Alex", "John", "   ", "Question", "Hallo!", True)
        self.assertEqual(result, ['Please Type EmailID'])

    def test_missing_first_name(self):
        result = validate_form("", "John", "abc@gmail.com", "Question", "Hallo!", True)
        self.assertEqual(result, ['Please Type First Name'])

    def test_missing_last_name(self):
        result = validate_form("Alex", "", "abc@gmail.com", "Question", "Hallo!", True)
        self.assertEqual(result, ['Please Type Last Name'])

    def test_missing_subject(self):
        result = validate_form("Alex", "John", "abc@gmail.com", "", "Hallo!", True)
        self.assertEqual(result, ['Please Type Subject'])

    def test_missing_message(self):
        result = validate_form("Alex", "John", "abc@gmail.com", "Question", "", True)
        self.assertEqual(result, ['Please Type Message'])

if __name__ == '__main__':
    unittest.main()
