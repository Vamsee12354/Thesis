import unittest
from implementation_manual import validate_form

class TestFormValidation(unittest.TestCase):
    def test_valid_form(self):
        result = validate_form("Alexa", "James", "abc@gmail.com", "Question", "Hallo!", True)
        self.assertEqual(result, "Form is valid. Details:Alexa,James,abc@gmail.com,Question,Hallo!,True")

    def test_invalid_privacy(self):
        result = validate_form("Alex", "John", "abc@gmail.net", "Question", "Hallo!", False)
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_empty_fields(self):
        result = validate_form("", "", "", "", "", "")
        self.assertEqual(result, ['Please Type First Name', 'Please Type Last Name', 'Please Type EmailID', 'Please Type Subject', 'Please Type Message', 'Please confirm the privacy policy'])

    def test_invalid_email_format(self):
        result = validate_form("John", "Doe", "invalid-email", "Subject", "Message", True)
        self.assertEqual(result, ["Email standards not followed"])

    def test_whitespace_fields(self):
        result = validate_form("   ", "   ", "   ", "   ", "   ", "   ")
        self.assertEqual(result, ['Please Type First Name', 'Please Type Last Name', 'Please Type EmailID', 'Please Type Subject', 'Please Type Message', 'Please confirm the privacy policy'])

    def test_multiple_errors(self):
        result = validate_form("", "Doe", "invalid-email", "", "Message", False)
        self.assertEqual(result, ['Please Type First Name', 'Email standards not followed', 'Please Type Subject', 'Please confirm the privacy policy'])

    def test_valid_form_with_whitespace(self):
        result = validate_form(" John ", " Doe ", " john@example.com ", " Subject ", " Message ", True)
        self.assertEqual(result, "Form is valid. Details:John,Doe,john@example.com,Subject,Message,True")

    def test_invalid_privacy_type(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "True")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_email_empty(self):
        result = validate_form("John", "Doe", "", "Subject", "Message", True)
        self.assertEqual(result, ["Please Type EmailID"])

    def test_invalid_email_whitespace(self):
        result = validate_form("John", "Doe", "   ", "Subject", "Message", True)
        self.assertEqual(result, ["Please Type EmailID"])

    def test_invalid_email_format_whitespace(self):
        result = validate_form("John", "Doe", " invalid@email ", "Subject", "Message", True)
        self.assertEqual(result, ["Email standards not followed"])

    def test_invalid_privacy_false(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", False)
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_none(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", None)
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_empty_string(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_zero(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", 0)
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_one(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", 1)
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_true(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "True")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_false(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "False")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_yes(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "Yes")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_no(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "No")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_one(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "1")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_zero(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "0")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_empty(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_whitespace(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "   ")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_invalid(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "invalid")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_true_lowercase(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "true")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_false_lowercase(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "false")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_yes_lowercase(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "yes")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_no_lowercase(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "no")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_one_lowercase(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "1")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_zero_lowercase(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "0")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_empty_lowercase(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_whitespace_lowercase(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "   ")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_invalid_lowercase(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "invalid")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_true_uppercase(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "TRUE")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_false_uppercase(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "FALSE")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_yes_uppercase(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "YES")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_no_uppercase(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "NO")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_one_uppercase(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "1")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_zero_uppercase(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "0")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_empty_uppercase(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_whitespace_uppercase(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "   ")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_invalid_uppercase(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "INVALID")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_true_mixed_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "TrUe")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_false_mixed_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "FaLsE")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_yes_mixed_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "YeS")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_no_mixed_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "No")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_one_mixed_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "1")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_zero_mixed_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "0")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_empty_mixed_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_whitespace_mixed_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "   ")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_invalid_mixed_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "InVaLiD")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_true_title_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "True")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_false_title_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "False")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_yes_title_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "Yes")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_no_title_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "No")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_one_title_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "1")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_zero_title_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "0")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_empty_title_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_whitespace_title_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "   ")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_invalid_title_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "Invalid")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_true_camel_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "true")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_false_camel_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "false")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_yes_camel_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "yes")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_no_camel_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "no")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_one_camel_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "1")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_zero_camel_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "0")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_empty_camel_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_whitespace_camel_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "   ")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_invalid_camel_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "invalid")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_true_snake_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "true")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_false_snake_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "false")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_yes_snake_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "yes")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_no_snake_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "no")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_one_snake_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "1")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_zero_snake_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "0")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_empty_snake_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_whitespace_snake_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "   ")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_invalid_snake_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "invalid")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_true_kebab_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "true")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_false_kebab_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "false")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_yes_kebab_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "yes")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_no_kebab_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "no")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_one_kebab_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "1")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_zero_kebab_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "0")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_empty_kebab_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_whitespace_kebab_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "   ")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_invalid_kebab_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "invalid")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_true_pascal_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "True")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_false_pascal_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "False")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_yes_pascal_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "Yes")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_no_pascal_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "No")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_one_pascal_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "1")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_zero_pascal_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "0")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_empty_pascal_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_whitespace_pascal_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "   ")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_invalid_pascal_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "Invalid")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_true_capital_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "TRUE")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_false_capital_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "FALSE")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_yes_capital_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "YES")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_no_capital_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "NO")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_one_capital_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "1")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_zero_capital_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "0")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_empty_capital_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_whitespace_capital_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "   ")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_invalid_capital_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "INVALID")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_true_lower_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "true")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_false_lower_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "false")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_yes_lower_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "yes")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_no_lower_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject", "Message", "no")
        self.assertEqual(result, ["Please confirm the privacy policy"])

    def test_invalid_privacy_string_one_lower_case(self):
        result = validate_form("John", "Doe", "john@example.com", "Subject",