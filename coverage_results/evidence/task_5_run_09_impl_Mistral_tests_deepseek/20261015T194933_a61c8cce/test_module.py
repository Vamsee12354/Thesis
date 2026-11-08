from implementation_manual import validate_form
import unittest


class TestFormValidation(unittest.TestCase):
    def test_valid_form(self):
        result = validate_form(
            "Alexa", "James", "abc@gmail.com", "Question", "Hallo!", True
        )
        expected = (
            "Form is valid. Details:Alexa,James,abc@gmail.com,Question,Hallo!,True"
        )
        self.assertEqual(result, expected)

    def test_rejecting_privacy_policy(self):
        result = validate_form(
            "Alex", "John", "abc@gmail.net", "Question", "Hallo!", False
        )
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_empty_body(self):
        result = validate_form("", "", "", "", "", "")
        expected = [
            "Please Type First Name",
            "Please Type Last Name",
            "Please Type EmailID",
            "Please Type Subject",
            "Please Type Message",
            "Please confirm the privacy policy",
        ]
        self.assertEqual(result, expected)

    def test_whitespace_only_fields(self):
        result = validate_form("   ", "  ", "  ", "  ", "  ", False)
        expected = [
            "Please Type First Name",
            "Please Type Last Name",
            "Please Type EmailID",
            "Please Type Subject",
            "Please Type Message",
            "Please confirm the privacy policy",
        ]
        self.assertEqual(result, expected)

    def test_invalid_email_format(self):
        result = validate_form(
            "John", "Doe", "invalid-email", "Subject", "Message", True
        )
        self.assertEqual(result, ["Email standards not followed"])

    def test_multiple_errors(self):
        result = validate_form("", "", "bad-email", "", "Message", False)
        expected = [
            "Please Type First Name",
            "Please Type Last Name",
            "Email standards not followed",
            "Please Type Subject",
            "Please confirm the privacy policy",
        ]
        self.assertEqual(result, expected)

    def test_valid_email_with_whitespace(self):
        result = validate_form(
            "John", "Doe", "  john@example.com  ", "Subject", "Message", True
        )
        expected = "Form is valid. Details:John,Doe,john@example.com,Subject,Message,True"
        self.assertEqual(result, expected)

    def test_non_boolean_privacy(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "True")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_error_message_order(self):
        result = validate_form("", "Doe", "bad-email", "", "", False)
        expected = [
            "Please Type First Name",
            "Email standards not followed",
            "Please Type Subject",
            "Please Type Message",
            "Please confirm the privacy policy",
        ]
        self.assertEqual(result, expected)