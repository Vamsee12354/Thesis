from implementation_manual import get_read_duration
import unittest

class TestGetReadDuration(unittest.TestCase):

    def test_empty_string_returns_one(self):
        self.assertEqual(get_read_duration(""), 1)

    def test_single_word_returns_one(self):
        self.assertEqual(get_read_duration("word"), 1)

    def test_two_words_returns_one(self):
        self.assertEqual(get_read_duration("word word"), 1)

    def test_fifty_words_returns_one(self):
        text = "word " * 50
        self.assertEqual(get_read_duration(text), 1)

    def test_four_hundred_fifty_words_returns_three(self):
        text = "word " * 450
        self.assertEqual(get_read_duration(text), 3)

    def test_four_hundred_ninety_nine_words_returns_three(self):
        text = "word " * 499
        self.assertEqual(get_read_duration(text), 3)

    def test_five_hundred_words_returns_three(self):
        text = "word " * 500
        self.assertEqual(get_read_duration(text), 3)

    def test_excessive_whitespace_returns_one(self):
        self.assertEqual(get_read_duration("   "), 1)

    def test_whitespace_with_words_returns_correct_duration(self):
        self.assertEqual(get_read_duration(" word   word  word "), 1)

    def test_non_latin_characters_with_spaces_returns_correct_duration(self):
        text = "你好 世界 " * 200
        self.assertEqual(get_read_duration(text), 2)

    def test_non_latin_characters_without_spaces_returns_one(self):
        self.assertEqual(get_read_duration("你好世界"), 1)

    def test_mixed_languages_with_spaces_returns_correct_duration(self):
        text = "Hello 你好 " * 200
        self.assertEqual(get_read_duration(text), 2)

    def test_very_long_text_returns_correct_duration(self):
        text = "word " * 10000
        self.assertEqual(get_read_duration(text), 50)

    def test_minimum_one_minute_for_short_text(self):
        self.assertEqual(get_read_duration("a"), 1)
        self.assertEqual(get_read_duration("a b"), 1)
        self.assertEqual(get_read_duration("a b c d e f"), 1)