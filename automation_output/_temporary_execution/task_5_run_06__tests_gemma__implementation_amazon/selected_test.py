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
        # Email is non-empty but doesn't match regex
        result = validate_form("John", "Doe", "invalid-email", "Subject", "Message", True)
        
        expected = ["Email standards not followed"]
        self.assertEqual(result, expected)

    def test_validate_form_empty_email_after_trimming(self):
        # AAA: Setup, Action, Verification
        # If email is empty after trimming, it should return "Please Type EmailID" and not regex error
        result = validate_form("John", "Doe", "   ", "Subject", "Message", True)
        
        expected = ["Please Type EmailID"]
        self.assertEqual(result, expected)

    def test_validate_form_privacy_false(self):
        # AAA: Setup, Action, Verification
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", False)
        
        expected = ["Please confirm the privacy policy"]
        self.assertEqual(result, expected)

    def test_validate_form_privacy_not_boolean(self):
        # AAA: Setup, Action, Verification
        # Specification says privacy must be True. If it's not (e.g. None or string), it fails.
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "NotABool")
        
        expected = ["Please confirm the privacy policy"]
        self.assertEqual(result, expected)

    def test_validate_form_multiple_errors_order(self):
        # AAA: Setup, Action, Verification
        # Testing specific order: First_Name, Last_Name, Email, Subject, Message, Privacy
        result = validate_form("", " ", "bad-email", "", "", False)
        
        expected = [
            'Please Type First Name',
            'Please Type Last Name',
            'Email standards not followed',
            'Please Type Subject',
            'Please Type Message',
            'Please confirm the privacy policy'
        ]
        self.assertEqual(result, expected)

    def test_validate_form_missing_last_name(self):
        # AAA: Setup, Action, Verification
        result = validate_form("John", "", "john@example.com", "Subject", "Message", True)
        
        expected = ["Please Type Last Name"]
        self.assertEqual(result, expected)

    def test_validate_form_missing_subject(self):
        # AAA: Setup, Action, Verification
        result = validate_form("John", "Doe", "john@example.com", "", "Message", True)
        
        expected = ["Please Type Subject"]
        self.assertEqual(result, expected)

    def test_validate_form_missing_message(self):
        # AAA: Setup, Action, Verification
        result = validate_form("John", "Doe", "john@example.com", "Subject", " ", True)
        
        expected = ["Please Type Message"]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()