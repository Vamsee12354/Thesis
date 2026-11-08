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

    def test_mixed_whitespace(self):
        text = "word \t word\nword\rword"
        self.assertEqual(get_read_duration(text), 1)

    def test_non_latin_characters(self):
        text = "中文 测试 文字"
        self.assertEqual(get_read_duration(text), 1)

    def test_long_text_with_punctuation(self):
        text = "This is a longer text. It contains multiple sentences! And some punctuation? Of course."
        self.assertEqual(get_read_duration(text), 1)

    def test_minimum_output(self):
        self.assertEqual(get_read_duration("a"), 1)