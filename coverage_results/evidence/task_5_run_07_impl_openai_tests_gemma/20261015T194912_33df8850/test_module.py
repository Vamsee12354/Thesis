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
        
        expected = "Form is valid. Details:John,Marston,john@example.com,Frage,Hallo!,True"
        self.assertEqual(result, expected)

    def test_validate_form_success_with_whitespace_trimming(self):
        # AAA: Setup, Action, Verification
        first_name = "  John  "
        last_name = "  Marston  "
        email = "  john@example.com  "
        subject = "  Frage  "
        message = "  Hallo!  "
        privacy = True
        
        result = validate_form(first_name, last_name, email, subject, message, privacy)
        
        expected = "Form is valid. Details:John,Marston,john@example.com,Frage,Hallo!,True"
        self.assertEqual(result, expected)

    def test_validate_form_all_fields_empty(self):
        # AAA: Setup, Action, Verification
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

    def test_validate_form_all_fields_whitespace_only(self):
        # AAA: Setup, Action, Verification
        result = validate_form(" ", " ", " ", " ", " ", "")
        
        expected = [
            'Please Type First Name',
            'Please Type Last Name',
            'Please Type EmailID',
            'Please Type Subject',
            'Please Type Message',
            'Please confirm the privacy policy'
        ]
        self.assertEqual(result, expected)

    def test_validate_form_invalid_email_format(self):
        # AAA: Setup, Action, Verification
        # Email is not empty but doesn't match regex
        result = validate_form("John", "Doe", "invalid-email", "Subject", "Message", True)
        
        expected = ["Email standards not followed"]
        self.assertEqual(result, expected)

    def test_validate_form_privacy_false(self):
        # AAA: Setup, Action, Verification
        result = validate_form("Alex", "John", "abc@gmail.net", "Question", "Hallo!", False)
        
        expected = ["Please confirm the privacy policy"]
        self.assertEqual(result, expected)

    def test_validate_form_privacy_not_boolean(self):
        # AAA: Setup, Action, Verification
        # Specification says privacy must be True. If it's not True (e.g. None or string), it fails.
        result = validate_form("John", "Doe", "john@test.com", "Hi", "Msg", "NotABool")
        
        expected = ["Please confirm the privacy policy"]
        self.assertEqual(result, expected)

    def test_validate_form_multiple_errors_order(self):
        # AAA: Setup, Action, Verification
        # Testing specific order: First_Name, Last_Name, Email, Subject, Message, Privacy
        result = validate_form("", "", "bademail", "", "", False)
        
        expected = [
            'Please Type First Name',
            'Please Type Last Name',
            'Email standards not followed',
            'Please Type Subject',
            'Please Type Message',
            'Please confirm the privacy policy'
        ]
        self.assertEqual(result, expected)

    def test_validate_form_email_empty_after_trim(self):
        # AAA: Setup, Action, Verification
        # If email is empty after trimming, it should return "Please Type EmailID" and not regex error
        result = validate_form("John", "Doe", "   ", "Subject", "Message", True)
        
        # Check if 'Please Type EmailID' is in the list and 'Email standards not followed' is not
        self.assertIn('Please Type EmailID', result)
        self.assertNotIn('Email standards not followed', result)

    def test_validate_form_single_error_first_name(self):
        # AAA: Setup, Action, Verification
        result = validate_form("", "Doe", "john@test.com", "Sub", "Msg", True)
        self.assertEqual(result, ["Please Type First Name"])

    def test_validate_form_single_error_last_name(self):
        # AAA: Setup, Action, Verification
        result = validate_form("John", "", "john@test.com", "Sub", "Msg", True)
        self.assertEqual(result, ["Please Type Last Name"])

    def test_validate_form_single_error_subject(self):
        # AAA: Setup, Action, Verification
        result = validate_form("John", "Doe", "john@test.com", "", "Msg", True)
        self.assertEqual(result, ["Please Type Subject"])

    def test_validate_form_single_error_message(self):
        # AAA: Setup, Action, Verification
        result = validate_form("John", "Doe", "john@test.com", "Sub", "", True)
        self.assertEqual(result, ["Please Type Message"])

if __name__ == '__main__':
    unittest.main()