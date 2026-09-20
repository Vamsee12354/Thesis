import unittest
from implementation_manual import validate_form

class TestValidateForm(unittest.TestCase):

    def test_validate_form_success(self):
        # Happy path: All fields valid
        first_name = "John"
        last_name = "Marston"
        email = "john@example.com"
        subject = "Frage"
        message = "Hallo!"
        privacy = True
        
        expected = "Form is valid. Details:John,Marston,john@example.com,Frage,Hallo!,True"
        result = validate_form(first_name, last_name, email, subject, message, privacy)
        self.assertEqual(result, expected)

    def test_validate_form_whitespace_success(self):
        # Happy path: Fields with whitespace that should be trimmed
        first_name = "  Alexa  "
        last_name = "  James  "
        email = "  abc@gmail.com  "
        subject = "  Question  "
        message = "  Hallo!  "
        privacy = True
        
        expected = "Form is valid. Details:Alexa,James,abc@gmail.com,Question,Hallo!,True"
        result = validate_form(first_name, last_name, email, subject, message, privacy)
        self.assertEqual(result, expected)

    def test_validate_form_all_empty_fields(self):
        # Edge case: All fields are empty strings
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

    def test_validate_form_all_whitespace_fields(self):
        # Edge case: All fields are only whitespace
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
        # Validation: Email exists but does not follow regex
        result = validate_form("John", "Doe", "invalid-email", "Subject", "Message", True)
        expected = ["Email standards not followed"]
        self.assertEqual(result, expected)

    def test_validate_form_empty_email_only(self):
        # Validation: Email is empty (should trigger EmailID error, not regex error)
        result = validate_form("John", "Doe", " ", "Subject", "Message", True)
        expected = ["Please Type EmailID"]
        self.assertEqual(result, expected)

    def test_validate_form_privacy_false(self):
        # Validation: Privacy is False
        result = validate_form("John", "Doe", "john@test.com", "Subject", "Message", False)
        expected = ["Please confirm the privacy policy"]
        self.assertEqual(result, expected)

    def test_validate_form_privacy_not_boolean(self):
        # Validation: Privacy is not True (e.g., None or string)
        result = validate_form("John", "Doe", "john@test.com", "Subject", "Message", "Yes")
        expected = ["Please confirm the privacy policy"]
        self.assertEqual(result, expected)

    def test_validate_form_multiple_errors_order(self):
        # Validation: Multiple errors must be returned in the specific order defined
        # Order: First_Name, Last_Name, Email, Subject, Message, Privacy
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

    def test_validate_form_missing_subject_and_message(self):
        # Validation: Specific missing fields
        result = validate_form("John", "Doe", "john@test.com", "", "", True)
        expected = [
            'Please Type Subject',
            'Please Type Message'
        ]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()