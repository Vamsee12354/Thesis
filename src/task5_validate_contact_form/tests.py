# Tests for task5_validate_contact_form
import unittest
from implementation_manual import validate_form


class Test_get_min(unittest.TestCase):
    def test_no_information(self):
        self.assertEqual(validate_form("","","","",""), "Please fill all the fields and try again")

    def test_null_values(self):
        self.assertEqual(validate_form(None,None,None,None,None), "Please fill all the fields and try again")

    def test_one_lettername(self):
        self.assertEqual(validate_form("va","abc@gmail.com","Question","Hallo!",True), f"Form is valid. Details are :{('va','abc@gmail.com','Question','Hallo!',True)} ")
    
    def test_normalfunctionalityof_name(self):
        self.assertEqual(validate_form("Alexa","abc@gmail.com","Question","Hallo!",True), f"Form is valid. Details are :{('Alexa','abc@gmail.com','Question','Hallo!',True)} ")
    
    def test_Full_name_3_words(self):
        self.assertEqual(validate_form("Alexa Google Home","abc@gmail.com","Question","Hallo!",True), f"Form is valid. Details are :{('Alexa Google Home','abc@gmail.com','Question','Hallo!',True)} ")

    def test_name_with_diff_language(self):
        self.assertEqual(validate_form("కలుపాటి వంశీ కుమార్","abc@gmail.com","Question","Hallo!",True), f"Form is valid. Details are :{('కలుపాటి వంశీ కుమార్','abc@gmail.com','Question','Hallo!',True)} ")
    
    def test_no_name_but_other_details(self):
        self.assertEqual(validate_form("","abc@gmail.com","Question","Hallo!",True), "Please fill all the fields and try again")

    def test_same_name_written(self):
        self.assertEqual(validate_form("Alex Alex Alex","abc@gmail.com","Question","Hallo!",True), f"Form is valid. Details are :{('Alex Alex Alex','abc@gmail.com','Question','Hallo!',True)} ")

    def test_email_functionality(self):
        self.assertEqual(validate_form("Alex","abc@gmail.com","Question","Hallo!",True), f"Form is valid. Details are :{('Alex','abc@gmail.com','Question','Hallo!',True)} ")

    def test_email_replacing_symbol_with_literalmeaning(self):
        self.assertEqual(validate_form("Alex","abcatgmail.com","Question","Hallo!",True), "Email is invalid")
    
    def test_try_different_extensions_email(self):
        self.assertEqual(validate_form("Alex","abc@gmail.net","Question","Hallo!",True), "Email is invalid")

    def test_try_different_extensions_email2(self):
        self.assertEqual(validate_form("Alex","abc@gmail.in","Question","Hallo!",True), "Email is invalid")
    
    def test_email_autheticity1(self):
        self.assertEqual(validate_form("Alex","abc abc def @gmail.net","Question","Hallo!",True), "Email is invalid")

    def test_email_autheticity2(self):
        self.assertEqual(validate_form("Alex","abc_def_@gmail.net","Question","Hallo!",True), "Email is invalid")

    def test_email_autheticity3(self):
        self.assertEqual(validate_form("Alex","12321345@gmail.net","Question","Hallo!",True), "Email is invalid")

    def test_privacy_Null(self):
        self.assertEqual(validate_form("Alex","abc@gmail.net","Question","Hallo!",None), "Please fill all the fields and try again")

    def test_privacy_reject(self):
        self.assertEqual(validate_form("Alex","abc@gmail.net","Question","Hallo!",False), "Please confirm the privacy policy")

    def test_subject(self):
        self.assertEqual(validate_form("Alex","abc@gmail.net","","Hallo!",True), "Please fill all the fields and try again")

    def test_message(self):
        self.assertEqual(validate_form("Alex","abc@gmail.net","Question","",True), "Please fill all the fields and try again")
        
    
if __name__ == "__main__":
    unittest.main()