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
        result = validate_form(" ", " ", " ", " ", " ", False)
        
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
        # Email is not empty but does not follow regex
        result = validate_form("John", "Doe", "invalid-email", "Subject", "Message", True)
        
        expected = ["Email standards not followed"]
        self.assertEqual(result, expected)

    def test_validate_form_invalid_privacy_false(self):
        # AAA: Setup, Action, Verification
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", False)
        
        expected = ["Please confirm the privacy policy"]
        self.assertEqual(result, expected)

    def test_validate_form_invalid_privacy_none(self):
        # AAA: Setup, Action, Verification
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", None)
        
        expected = ["Please confirm the privacy policy"]
        self.assertEqual(result, expected)

    def test_validate_form_multiple_errors_order(self):
        # AAA: Setup, Action, Verification
        # Testing specific order: First, Last, Email (empty), Subject, Message, Privacy
        result = validate_form("", " ", "", "", " ", False)
        
        expected = [
            'Please Type First Name',
            'Please Type Last Name',
            'Please Type EmailID',
            'Please Type Subject',
            'Please Type Message',
            'Please confirm the privacy policy'
        ]
        self.assertEqual(result, expected)

    def test_validate_form_email_empty_after_trim(self):
        # AAA: Setup, Action, Verification
        # If email is empty after trimming, it should return "Please Type EmailID" 
        # and NOT "Email standards not followed"
        result = validate_form("John", "Doe", "   ", "Subject", "Message", True)
        
        self.assertIn("Please Type EmailID", result)
        self.assertNotIn("Email standards not followed", result)

    def test_validate_form_email_invalid_format_with_other_errors(self):
        # AAA: Setup, Action, Verification
        # First name empty, email invalid format
        result = validate_form("", "Doe", "bademail", "Subject", "Message", True)
        
        expected = [
            'Please Type First Name',
            'Email standards not followed'
        ]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()