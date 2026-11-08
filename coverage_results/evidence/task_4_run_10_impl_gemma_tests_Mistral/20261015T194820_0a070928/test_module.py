from implementation_manual import get_read_duration
import unittest

class TestGetReadDuration(unittest.TestCase):

    def test_empty_string_returns_one(self):
        self.assertEqual(get_read_duration(""), 1)

    def test_excessive_whitespace_returns_one(self):
        self.assertEqual(get_read_duration("   "), 1)
        self.assertEqual(get_read_duration("\t\n"), 1)

    def test_single_word_returns_one(self):
        self.assertEqual(get_read_duration("word"), 1)
        self.assertEqual(get_read_duration("Hello"), 1)

    def test_two_words_returns_one(self):
        self.assertEqual(get_read_duration("Hello world"), 1)

    def test_fifty_words_returns_one(self):
        text = "word " * 50
        self.assertEqual(get_read_duration(text), 1)

    def test_fifty_one_words_returns_two(self):
        text = "word " * 51
        self.assertEqual(get_read_duration(text), 2)

    def test_400_words_returns_two(self):
        text = "word " * 400
        self.assertEqual(get_read_duration(text), 2)

    def test_401_words_returns_three(self):
        text = "word " * 401
        self.assertEqual(get_read_duration(text), 3)

    def test_450_words_returns_three(self):
        text = "word " * 450
        self.assertEqual(get_read_duration(text), 3)

    def test_non_latin_characters(self):
        text = "你好 世界 " * 100
        self.assertEqual(get_read_duration(text), 2)

    def test_mixed_whitespace(self):
        text = "word\tword\nword  word"
        self.assertEqual(get_read_duration(text), 1)

    def test_punctuation_handling(self):
        text = "Hello, world! How are you?"
        self.assertEqual(get_read_duration(text), 1)

    def test_long_text_with_newlines(self):
        text = "word\n" * 600
        self.assertEqual(get_read_duration(text), 3)