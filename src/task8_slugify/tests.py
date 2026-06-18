# Tests for task8_slugify
import unittest
from implementation_manual import slugify_manual

class Test_slugify_text(unittest.TestCase):

    def test_no_text(self):
        self.assertEqual(slugify_manual(''),None)
     
    def test_functionality(self):
        self.assertEqual(slugify_manual('Writing slugify code helloWorld'),'writing-slugify-code-helloworld')

    def test_all_capitals(self):
        self.assertEqual(slugify_manual('THE TEXTIS ALL CAPS'),'the-textis-all-caps')

    def test_sentence_with_no_space(self):
        self.assertEqual(slugify_manual('WritingslugifycodehelloWorld'),'writing-slugify-code-helloworld')

    def test_sentence_with_punctuations(self):
        self.assertEqual(slugify_manual('Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam'),'lorem-ipsum-dolor-sit-amet-consetetur-sadipscing-elitr-sed-diam')

    def test_single_word(self):
        self.assertEqual(slugify_manual('Lorem'),'lorem')
        
    def test_spaces_single_word(self):
        self.assertEqual(slugify_manual('                      Lorem'),'lorem')

    def test_repeated_spaces_between_words(self):
        self.assertEqual(slugify_manual('Lorem          ipsum              dolor sit amet,                  consetetur sadipscing                elitr, sed                   diam'),'lorem-ipsum-dolor-sit-amet-consetetur-sadipscing-elitr-sed-diam')

    def test_letters_spaces(self):
        self.assertEqual(slugify_manual('L o r e m i p s u m d o l o r s i t a m e t , c o n s e t e t u r'),'loremipsumdolorsitametconsetetur')

    def test_different_language(self):
        self.assertEqual(slugify_manual('Für die WMCE wählen Radiosprecher von Weltmusikprogrammen aus 24 Europäischen Ländern jeden Monat ihre persönliche Top 10 der aktuellen Albumveröffentlichungen.'),'für-die-wmce-wählen-radiosprecher-von-weltmusikprogrammen-aus-24-europäischen-ländern-jeden-monat-ihre-persönliche-top-10-der-aktuellen-albumveröffentlichungen')

    def already_slugified(self):
        self.assertEqual(slugify_manual('writing-slugify-code-helloworld'),'writing-slugify-code-helloworld')

    def test_multiple_batches_text(self):
        self.assertEqual(slugify_manual('WritingslugifycodehelloWorld'),'writingslugifycodehelloworld')

    def test_symbols_inbetween_text(self):
        self.assertEqual(slugify_manual('Lorem @##$  ipsum &&&!@ dolor &!&@#! sit *!&@!# amet !@@#!@!/., consetetur $%#$#% sadipscing ,.,.><<> elitr $%%%^^^^^, sed diam'),'lorem-ipsum-dolor-sit-amet-consetetur-sadipscing-elitr-sed-diam')
        
    def test_ignore(self):
        self.assertEqual(slugify_manual("hello%world", lowercase=True, ignore="%", truncate=None),"hello%world")

    def test_separator(self):
        self.assertEqual(slugify_manual("hello%  world",separator='+', ignore="%", truncate=None),"hello%+world")

    def test_truncate(self):
        self.assertEqual(slugify_manual("hello%  world",separator='+', ignore="%", truncate=2),"")
    
        self.assertEqual(slugify_manual("Writing slugify code helloWorld", separator='-', truncate=14),"writing")




     



    
     

    




if __name__ == "__main__":
    unittest.main()