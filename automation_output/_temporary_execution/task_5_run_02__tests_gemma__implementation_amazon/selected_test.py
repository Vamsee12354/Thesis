import unittest
from implementation_manual import validate_form

class TestValidateForm(unittest.TestCase):

    def test_valid_form_submission(self):
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

    def test_valid_form_with_whitespace_trimming(self):
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

    def test_all_fields_empty(self):
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

    def test_all_fields_whitespace_only(self):
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

    def test_invalid_email_format(self):
        # AAA: Setup, Action, Verification
        # Email is non-empty but doesn't match regex
        result = validate_form("John", "Doe", "invalid-email", "Subject", "Message", True)
        
        expected = ["Email standards not followed"]
        self.assertEqual(result, expected)

    def test_empty_email_error_message(self):
        # AAA: Setup, Action, Verification
        # If email is empty after trimming, it should return "Please Type EmailID" 
        # and NOT "Email standards not followed"
        result = validate_form("John", "Doe", "   ", "Subject", "Message", True)
        
        self.assertIn("Please Type EmailID", result)
        self.assertNotIn("Email standards not followed", result)

    def test_privacy_policy_false(self):
        # AAA: Setup, Action, Verification
        result = validate_form("Alex", "John", "abc@gmail.net", "Question", "Hallo!", False)
        
        expected = ["Please confirm the privacy policy"]
        self.assertEqual(result, expected)

    def test_privacy_policy_not_boolean(self):
        # AAA: Setup, Action, Verification
        # Privacy must be True. If it's something else (like None or 0), it fails.
        result = validate_form("John", "Doe", "john@test.com", "Hi", "Msg", None)
        
        expected = ["Please confirm the privacy policy"]
        self.assertEqual(result, expected)

    def test_multiple_errors_order(self):
        # AAA: Setup, Action, Verification
        # Testing specific order: First_Name, Last_Name, Email, Subject, Message, Privacy
        result = validate_form("", " ", "bademail", "", "", False)
        
        expected = [
            'Please Type First Name',
            'Please Type Last Name',
            'Email standards not followed',
            'Please Type Subject',
            'Please Type Message',
            'Please confirm the privacy policy'
        ]
        self.assertEqual(result, expected)

    def test_email_regex_edge_cases(self):
        # AAA: Setup, Action, Verification
        # Test various invalid email formats
        invalid_emails = ["@example.com", "john@", "john@example", "john.example.com"]
        
        for email in invalid_emails:
            result = validate_form("John", "Doe", email, "Sub", "Msg", True)
            self.assertEqual(result, ["Email standards not followed"])

if __name__ == '__main__':
    unittest.main()