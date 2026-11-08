import unittest
from implementation_manual import get_read_duration

class TestGetReadDuration(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(get_read_duration(""), 1)

    def test_whitespace_only(self):
        self.assertEqual(get_read_duration("   "), 1)

    def test_single_word(self):
        self.assertEqual(get_read_duration("word"), 1)

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
        text = "这是一个测试 " * 50  # 50 Chinese words
        self.assertEqual(get_read_duration(text.strip()), 1)

    def test_mixed_whitespace(self):
        text = "word\nword\tword  word"
        self.assertEqual(get_read_duration(text), 1)

    def test_long_text_with_various_whitespace(self):
        text = ("word " * 199) + "\nword\tword"
        self.assertEqual(get_read_duration(text), 2)