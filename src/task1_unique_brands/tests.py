import unittest
from implementation_manual import get_unique

class Test_unique_brands(unittest.TestCase):

    def test_list_is_empty(self):
        self.assertEqual(get_unique([]),None)

    def test_if_list_unique(self):
        self.assertEqual(get_unique([{"brand":"toyota"},{"brand":"bmw"},{"brand":"mercedes"}]),
        ["Toyota","Bmw","Mercedes"])

    def test_capital_can_distinguish_uniqueness(self):
        self.assertEqual(get_unique([{"brand":"Toyota"},{"brand":"Bmw"},{"brand":"toyota"},{"brand":"bmw"}]),
        ["Toyota","Bmw"])

    def test_numbers_uniqueness(self):
        self.assertEqual(get_unique([{"brand":1},{"brand":1},{"brand":1},{"brand":3},{"brand":3},{"brand":3}]), [1,3])

    def test_symbols_uniqueness(self):
        self.assertEqual(get_unique([{"brand":"@"},{"brand":"!"},{"brand":"@"},{"brand":"$"},{"brand":"&"},{"brand":"@"},{"brand":"#"},{"brand":"$"},{"brand":"%"},{"brand":"^"},{"brand":"&"}]),
        ["@","!","$","&","#","%","^"])

    def test_multiple_characters(self):
        self.assertEqual(get_unique([{"brand":"!@#"},{"brand":"#@$@!"},{"brand":"#@$@!"},{"brand":"32421"},{"brand":"abcqw"},{"brand":"abcqw"},{"brand":"bmw"}]),
        ["!@#","#@$@!","32421","Abcqw","Bmw"])

    def test_japenese_words(self):
        self.assertEqual(get_unique([{"brand":"おはようございます"},{"brand":"こんばんは"},{"brand":"おはようございます"},{"brand":"すみません"},{"brand":"ありがとうございます"},{"brand":"すみません"},{"brand":"ごめんなさい"},{"brand":"こんにちは"}]),
        ["おはようございます","こんばんは","すみません","ありがとうございます","ごめんなさい","こんにちは"])

    def check_same_letter_uniqueness(self):
        self.assertEqual(get_unique([{"brand":"a"},{"brand":"a"},{"brand":"a"}]),
        ["A"])

    def test_with_nike(self):
        self.assertEqual(get_unique([{'brand':'nike'},{'brand':'Nike'},{'brand':'nIke'},{'brand':'nikE'}]),['Nike'])

    def test_with_nike(self):
        self.assertEqual(get_unique([{'brand':None},{'brand':'Sike'},{'brand':'nIke'},{'brand':None}]),['Sike'])

if __name__ == "__main__":
    unittest.main()
