import unittest
from implementation_manual import validate_form

class TestValidateForm(unittest.TestCase):

    def test_validate_form_success(self):
        # AAA: Setup, Action, Verification
        first_name = "John"
        last_name = "Marston"
        email = "john@example.com"
        subject = "Frage"
        message = "Hallo!"
        privacy = True
        
        result = validate_form(first_name, last_name, email, subject, message, privacy)
        
        self.assertEqual(result, "Form is valid. Details:John,Marston,john@example.com,Frage,Hallo!,True")

    def test_validate_form_success_with_whitespace(self):
        # Testing that whitespace is trimmed correctly for valid inputs
        result = validate_form("  Alexa  ", "  James  ", "  abc@gmail.com  ", "Question", "Hallo!", True)
        self.assertEqual(result, "Form is valid. Details:Alexa,James,abc@gmail.com,Question,Hallo!,True")

    def test_validate_form_all_fields_empty(self):
        # AAA: Setup, Action, Verification
        result = validate_form("", "", "", "", "", "")
        expected_errors = [
            'Please Type First Name',
            'Please Type Last Name',
            'Please Type EmailID',
            'Please Type Subject',
            'Please Type Message',
            'Please confirm the privacy policy'
        ]
        self.assertEqual(result, expected_errors)

    def test_validate_form_whitespace_only_fields(self):
        # AAA: Setup, Action, Verification
        result = validate_form("   ", "\t", "\n", " ", "", False)
        expected_errors = [
            'Please Type First Name',
            'Please Type Last Name',
            'Please Type EmailID',
            'Please Type Subject',
            'Please Type Message',
            'Please confirm the privacy policy'
        ]
        self.assertEqual(result, expected_errors)

    def test_validate_form_invalid_email_format(self):
        # AAA: Setup, Action, Verification
        # Email is not empty but does not follow regex
        result = validate_form("John", "Doe", "invalid-email", "Subject", "Message", True)
        self.assertEqual(result, ["Email standards not followed"])

    def test_validate_form_empty_email_error_message(self):
        # AAA: Setup, Action, Verification
        # If email is empty after trimming, it should return "Please Type EmailID"
        result = validate_form("John", "Doe", "   ", "Subject", "Message", True)
        self.assertEqual(result, ["Please Type EmailID"])

    def test_validate_form_privacy_false(self):
        # AAA: Setup, Action, Verification
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", False)
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_validate_form_privacy_not_boolean(self):
        # AAA: Setup, Action, Verification
        # Privacy must be True. If it's not True (e.g., None or string), it fails.
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "True")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_validate_form_multiple_errors_order(self):
        # AAA: Setup, Action, Verification
        # Testing specific order: First_Name, Last_Name, Email, Subject, Message, Privacy
        result = validate_form("", "", "bad_email", "", "", False)
        expected_errors = [
            'Please Type First Name',
            'Please Type Last Name',
            'Email standards not followed',
            'Please Type Subject',
            'Please Type Message',
            'Please confirm the privacy policy'
        ]
        self.assertEqual(result, expected_errors)

    def test_validate_form_missing_subject_and_message(self):
        # AAA: Setup, Action, Verification
        result = validate_form("John", "Doe", "john@example.com", "", "", True)
        expected_errors = [
            'Please Type Subject',
            'Please Type Message'
        ]
        self.assertEqual(result, expected_errors)

if __name__ == '__main__':
    unittest.main()