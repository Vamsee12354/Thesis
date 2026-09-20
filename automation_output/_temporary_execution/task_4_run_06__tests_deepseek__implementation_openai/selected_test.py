import unittest
from implementation_manual import get_read_duration

class TestGetReadDuration(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(get_read_duration(""), 1)

    def test_whitespace_only(self):
        self.assertEqual(get_read_duration("   "), 1)

    def test_single_word(self):
        self.assertEqual(get_read_duration("word"), 1)

    def test_short_paragraph(self):
        self.assertEqual(get_read_duration("This is a short paragraph with five words."), 1)

    def test_exactly_200_words(self):
        text = "word " * 200
        self.assertEqual(get_read_duration(text.strip()), 1)

    def test_201_words(self):
        text = "word " * 201
        self.assertEqual(get_read_duration(text.strip()), 2)

    def test_450_words(self):
        text = "word " * 450
        self.assertEqual(get_read_duration(text.strip()), 3)

    def test_non_latin_characters(self):
        self.assertEqual(get_read_duration("汉字 汉字 汉字"), 1)

    def test_mixed_content(self):
        text = "This is a test with 汉字 and English words."
        self.assertEqual(get_read_duration(text), 1)

    def test_punctuation_handling(self):
        text = "This, is. a! test? with: punctuation;"
        self.assertEqual(get_read_duration(text), 1)

    def test_newlines_and_tabs(self):
        text = "This\nhas\tmultiple whitespace\tcharacters\n"
        self.assertEqual(get_read_duration(text), 1)