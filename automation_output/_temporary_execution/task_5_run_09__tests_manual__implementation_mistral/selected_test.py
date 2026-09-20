# Tests for task5_validate_contact_form
import unittest
from implementation_manual import validate_form


class Test_get_min(unittest.TestCase):
    def test_no_information(self):
        self.assertEqual(validate_form("","","","","",""), ['Please Type First Name', 'Please Type Last Name', 'Please Type EmailID', 'Please Type Subject', 'Please Type Message', 'Please confirm the privacy policy'])

    def test_null_values(self):
        self.assertEqual(validate_form(None,None,None,None,None,None), ['Please Type First Name', 'Please Type Last Name', 'Please Type EmailID', 'Please Type Subject', 'Please Type Message', 'Please confirm the privacy policy'])

    def test_one_lettername(self):
        self.assertEqual(validate_form("va","se","abc@gmail.com","Question","Hallo!",True), "Form is valid. Details:va,se,abc@gmail.com,Question,Hallo!,True")
    
    def test_normalfunctionalityof_name(self):
        self.assertEqual(validate_form("Alexa","James","abc@gmail.com","Question","Hallo!",True), "Form is valid. Details:Alexa,James,abc@gmail.com,Question,Hallo!,True")
    
    def test_longname(self):
        self.assertEqual(validate_form("Alexa Google Home","Echo Dot","abc@gmail.com","Question","Hallo!",True), "Form is valid. Details:Alexa Google Home,Echo Dot,abc@gmail.com,Question,Hallo!,True")

    def test_name_with_diff_language(self):
        self.assertEqual(validate_form("కలుపాట","వంశీ కుమార్","abc@gmail.com","Question","Hallo!",True), "Form is valid. Details:కలుపాట,వంశీ కుమార్,abc@gmail.com,Question,Hallo!,True")
    
    def test_no_firstname_but_other_details(self):
        self.assertEqual(validate_form("","James","abc@gmail.com","Question","Hallo!",True), ['Please Type First Name'])

    def test_same_name_written(self):
        self.assertEqual(validate_form("Alex","Alex","abc@gmail.com","Question","Hallo!",True), "Form is valid. Details:Alex,Alex,abc@gmail.com,Question,Hallo!,True")

    def test_email_functionality(self):
        self.assertEqual(validate_form("Alex","James","abc@gmail.com","Question","Hallo!",True), "Form is valid. Details:Alex,James,abc@gmail.com,Question,Hallo!,True")

    def test_email_replacing_symbol_with_literalmeaning(self):
        self.assertEqual(validate_form("Alex","James","abcatgmail.com","Question","Hallo!",True), ["Email standards not followed"])
    
    def test_try_different_extensions_email(self):
        self.assertEqual(validate_form("Alex","James","abc@gmail.net","Question","Hallo!",True), "Form is valid. Details:Alex,James,abc@gmail.net,Question,Hallo!,True")

    def test_try_different_extensions_email2(self):
        self.assertEqual(validate_form("Alex","James","abc@gmail.in","Question","Hallo!",True), "Form is valid. Details:Alex,James,abc@gmail.in,Question,Hallo!,True")
    
    def test_email_autheticity1(self):
        self.assertEqual(validate_form("Alex","James","abc abc def @gmail.net","Question","Hallo!",True), ["Email standards not followed"])

    def test_email_autheticity2(self):
        self.assertEqual(validate_form("Alex","James","abc_def_@gmail.net","Question","Hallo!",True), "Form is valid. Details:Alex,James,abc_def_@gmail.net,Question,Hallo!,True")

    def test_email_autheticity3(self):
        self.assertEqual(validate_form("Alex","James","12321345@gmail.net","Question","Hallo!",True), "Form is valid. Details:Alex,James,12321345@gmail.net,Question,Hallo!,True")

    def test_privacy_Null(self):
        self.assertEqual(validate_form("Alex","James","abc@gmail.net","Question","Hallo!",None), ['Please confirm the privacy policy'])

    def test_privacy_reject(self):
        self.assertEqual(validate_form("Alex","James","abc@gmail.net","Question","Hallo!",False), ["Please confirm the privacy policy"])

    def test_subject(self):
        self.assertEqual(validate_form("Alex","James","abc@gmail.net","","Hallo!",True), ['Please Type Subject'])

    def test_message(self):
        self.assertEqual(validate_form("Alex","James","abc@gmail.net","Question","",True), ['Please Type Message'])
        
    
if __name__ == "__main__":
    unittest.main()