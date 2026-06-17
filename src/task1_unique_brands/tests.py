import unittest
from implementation_manual import get_unique

class Test_unique_brands(unittest.TestCase):

    def test_list_is_empty(self):
        self.assertEqual(get_unique([]),[])

    def test_if_list_unique(self):
        self.assertEqual(get_unique(["toyota","bmw","mercedes"]),
        ["toyota","bmw","mercedes"])

    def test_capital_can_distinguish_uniqueness(self):
        self.assertEqual(get_unique(["Toyota","Bmw","toyota","bmw"]),
        ["Toyota","Bmw"])

    def test_numbers_uniqueness(self):
        self.assertEqual(get_unique([1,1,1,3,3,3]), [1,3])

    def test_symbols_uniqueness(self):
        self.assertEqual(get_unique(["@","!","@","$","&","@","#","$","%","^","&"]),
        ["@","!","$","&","#","%","^"])

    def test_multiple_characters(self):
        self.assertEqual(get_unique(['!@#','#@$@!','#@$@!','32421','abcqw','abcqw','bmw']),
        ['!@#','#@$@!','32421','abcqw','bmw'])

    def test_japenese_words(self):
        self.assertEqual(get_unique(["おはようございます","こんばんは","おはようございます","すみません","ありがとうございます","すみません","ごめんなさい","こんにちは"]),
        ["おはようございます","こんばんは","すみません","ありがとうございます","ごめんなさい","こんにちは"])

    def check_same_letter_uniqueness(self):
        self.assertEqual(get_unique(['a','a','a']),'a')

if __name__ == "__main__":
    unittest.main()