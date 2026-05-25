# Tests for task5_validate_contact_form
import unittest
from implementation_manual import validate_form


class Test_get_min(unittest.TestCase):
    def test_no_information(self):
        self.assertEqual(validate_form("","",""), False)

    def test_null_values(self):
        self.assertEqual(validate_form(None,None,None), False)

    def test_one_lettername(self):
        self.assertEqual(validate_form("va","abc@gmail.com","9123912321"),False)
    
    def test_normalfunctionalityof_name(self):
        self.assertEqual(validate_form("vamsee","abc@gmail.com","9123912321"),True)
    
    def test_Full_name_3_words(self):
        self.assertEqual(validate_form("kalupati vamsee kumar","abc@gmail.com","9123912321"),True)

    def test_name_with_diff_language(self):
        self.assertEqual(validate_form("కలుపాటి వంశీ కుమార్","abc@gmail.com","9123912321"),True)
    
    def test_no_name_but_other_details(self):
        self.assertEqual(validate_form("","abc@gmail.com","9123912321"),False)

    def test_same_name_written(self):
        self.assertEqual(validate_form("Alex Alex Alex","abc@gmail.com","9123912321"),True)

    def test_email_functionality(self):
        self.assertEqual(validate_form("Alex","abc@gmail.com","9123912321"),True)

    def test_email_replacing_symbol_with_literalmeaning(self):
        self.assertEqual(validate_form("Alex","abcatgmail.com","9123912321"),False)
    
    def test_try_different_extensions_email(self):
        self.assertEqual(validate_form("Alex","abc@gmail.net","9123912321"),False)

    def test_try_different_extensions_email2(self):
        self.assertEqual(validate_form("Alex","abc@gmail.in","9123912321"),False)
    
    def test_email_autheticity1(self):
        self.assertEqual(validate_form("Alex","abc abc def @gmail.net","9123912321"),False)

    def test_email_autheticity2(self):
        self.assertEqual(validate_form("Alex","abc_def_@gmail.net","9123912321"),False)

    def test_email_autheticity3(self):
        self.assertEqual(validate_form("Alex","12321345@gmail.net","9123912321"),True)

    def test_phone_less_digits(self):
        self.assertEqual(validate_form("Alex","abc@gmail.net","123"),False)

    def test_phone_spaces(self):
        self.assertEqual(validate_form("Alex","abc@gmail.net","9821 2198 22"),False)

    def test_phone_less_digits(self):
        self.assertEqual(validate_form("Alex","abc@gmail.net","123"),False)

    def test_phone_country_cpde(self):
        self.assertEqual(validate_form("Alex","abc@gmail.net","+49 9123912321"),False)

    def test_phone_country_cpde_withoutspace(self):
        self.assertEqual(validate_form("Alex","abc@gmail.net","+499123912321"),False)

    def test_phone_more_digits(self):
        self.assertEqual(validate_form("Alex","abc@gmail.net","918218328812388124832812312313"),False)
        
    
if __name__ == "__main__":
    unittest.main()