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
        first_name = "  Jane  "
        last_name = "Doe"
        email = " jane@test.com "
        subject = "Hello"
        message = "World"
        privacy = True
        
        result = validate_form(first_name, last_name, email, subject, message, privacy)
        
        expected = "Form is valid. Details:Jane,Doe,jane@test.com,Hello,World,True"
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

    def test_missing_first_name(self):
        # AAA: Setup, Action, Verification
        result = validate_form(" ", "Doe", "test@test.com", "Sub", "Msg", True)
        self.assertIn('Please Type First Name', result)

    def test_missing_last_name(self):
        # AAA: Setup, Action, Verification
        result = validate_form("John", " ", "test@test.com", "Sub", "Msg", True)
        self.assertIn('Please Type Last Name', result)

    def test_empty_email_after_trimming(self):
        # AAA: Setup, Action, Verification
        result = validate_form("John", "Doe", "   ", "Sub", "Msg", True)
        self.assertIn('Please Type EmailID', result)

    def test_invalid_email_format(self):
        # AAA: Setup, Action, Verification
        result = validate_form("John", "Doe", "invalid-email", "Sub", "Msg", True)
        self.assertIn('Email standards not followed', result)

    def test_missing_subject(self):
        # AAA: Setup, Action, Verification
        result = validate_form("John", "Doe", "test@test.com", "", "Msg", True)
        self.assertIn('Please Type Subject', result)

    def test_missing_message(self):
        # AAA: Setup, Action, Verification
        result = validate_form("John", "Doe", "test@test.com", "Sub", "   ", True)
        self.assertIn('Please Type Message', result)

    def test_privacy_not_true(self):
        # AAA: Setup, Action, Verification
        result = validate_form("John", "Doe", "test@test.com", "Sub", "Msg", False)
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_privacy_not_boolean(self):
        # AAA: Setup, Action, Verification
        result = validate_form("John", "Doe", "test@test.com", "Sub", "Msg", "True")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_multiple_errors_order(self):
        # AAA: Setup, Action, Verification
        # Testing order: First_Name, Last_Name, Email, Subject, Message, Privacy
        result = validate_form("", "", "bad-email", "", "", False)
        
        expected = [
            'Please Type First Name',
            'Please Type Last Name',
            'Email standards not followed',
            'Please Type Subject',
            'Please Type Message',
            'Please confirm the privacy policy'
        ]
        self.assertEqual(result, expected)

    def test_email_empty_does_not_trigger_regex_error(self):
        # AAA: Setup, Action, Verification
        # If email is empty, it should only return 'Please Type EmailID', not 'Email standards not followed'
        result = validate_form("John", "Doe", " ", "Sub", "Msg", True)
        self.assertIn('Please Type EmailID', result)
        self.assertNotIn('Email standards not followed', result)

if __name__ == '__main__':
    unittest.main()