from implementation_manual import validate_form
import unittest

class TestValidateForm(unittest.TestCase):

    def test_normal_functionality(self):
        result = validate_form("Alexa", "James", "abc@gmail.com", "Question", "Hallo!", True)
        expected = "Form is valid. Details:Alexa,James,abc@gmail.com,Question,Hallo!,True"
        self.assertEqual(result, expected)

    def test_empty_fields(self):
        result = validate_form("", "", "", "", "", "")
        expected = [
            "Please Type First Name",
            "Please Type Last Name",
            "Please Type EmailID",
            "Please Type Subject",
            "Please Type Message",
            "Please confirm the privacy policy"
        ]
        self.assertEqual(result, expected)

    def test_whitespace_only_fields(self):
        result = validate_form("   ", "   ", "   ", "   ", "   ", False)
        expected = [
            "Please Type First Name",
            "Please Type Last Name",
            "Please Type EmailID",
            "Please Type Subject",
            "Please Type Message",
            "Please confirm the privacy policy"
        ]
        self.assertEqual(result, expected)

    def test_missing_first_name(self):
        result = validate_form("", "Doe", "john@example.com", "Query", "Hello", True)
        expected = ["Please Type First Name"]
        self.assertEqual(result, expected)

    def test_missing_last_name(self):
        result = validate_form("John", "", "john@example.com", "Query", "Hello", True)
        expected = ["Please Type Last Name"]
        self.assertEqual(result, expected)

    def test_missing_email(self):
        result = validate_form("John", "Doe", "", "Query", "Hello", True)
        expected = ["Please Type EmailID"]
        self.assertEqual(result, expected)

    def test_invalid_email_format(self):
        result = validate_form("John", "Doe", "invalid-email", "Query", "Hello", True)
        expected = ["Email standards not followed"]
        self.assertEqual(result, expected)

    def test_missing_subject(self):
        result = validate_form("John", "Doe", "john@example.com", "", "Hello", True)
        expected = ["Please Type Subject"]
        self.assertEqual(result, expected)

    def test_missing_message(self):
        result = validate_form("John", "Doe", "john@example.com", "Query", "", True)
        expected = ["Please Type Message"]
        self.assertEqual(result, expected)

    def test_privacy_false(self):
        result = validate_form("John", "Doe", "john@example.com", "Query", "Hello", False)
        expected = ["Please confirm the privacy policy"]
        self.assertEqual(result, expected)

    def test_privacy_not_boolean(self):
        result = validate_form("John", "Doe", "john@example.com", "Query", "Hello", "True")
        expected = ["Please confirm the privacy policy"]
        self.assertEqual(result, expected)

    def test_multiple_errors(self):
        result = validate_form("", "", "invalid-email", "", "", False)
        expected = [
            "Please Type First Name",
            "Please Type Last Name",
            "Please Type EmailID",
            "Please Type Subject",
            "Please Type Message",
            "Please confirm the privacy policy"
        ]
        self.assertEqual(result, expected)

    def test_email_with_whitespace(self):
        result = validate_form("John", "Doe", "  john@example.com  ", "Query", "Hello", True)
        expected = "Form is valid. Details:John,Doe,john@example.com,Query,Hello,True"
        self.assertEqual(result, expected)

    def test_email_empty_after_trim(self):
        result = validate_form("John", "Doe", "   ", "Query", "Hello", True)
        expected = ["Please Type EmailID"]
        self.assertEqual(result, expected)

    def test_all_fields_valid_with_whitespace(self):
        result = validate_form("  John  ", "  Doe  ", "  john@example.com  ", "  Query  ", "  Hello  ", True)
        expected = "Form is valid. Details:John,Doe,john@example.com,Query,Hello,True"
        self.assertEqual(result, expected)