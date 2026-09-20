from implementation_manual import get_read_duration
import unittest

class TestGetReadDuration(unittest.TestCase):

    def test_empty_string(self):
        result = get_read_duration("")
        self.assertEqual(result, 1)

    def test_excessive_whitespace(self):
        result = get_read_duration("   ")
        self.assertEqual(result, 1)

    def test_single_word(self):
        result = get_read_duration("word")
        self.assertEqual(result, 1)

    def test_two_words(self):
        result = get_read_duration("word word")
        self.assertEqual(result, 1)

    def test_50_words(self):
        words = "word " * 50
        result = get_read_duration(words)
        self.assertEqual(result, 1)

    def test_200_words(self):
        words = "word " * 200
        result = get_read_duration(words)
        self.assertEqual(result, 1)

    def test_201_words(self):
        words = "word " * 201
        result = get_read_duration(words)
        self.assertEqual(result, 2)

    def test_400_words(self):
        words = "word " * 400
        result = get_read_duration(words)
        self.assertEqual(result, 2)

    def test_450_words(self):
        words = "word " * 450
        result = get_read_duration(words)
        self.assertEqual(result, 3)

    def test_non_latin_characters(self):
        result = get_read_duration("你好 世界 这是 中文")
        self.assertEqual(result, 1)

    def test_mixed_whitespace(self):
        result = get_read_duration("word\tword\nword  word")
        self.assertEqual(result, 1)

    def test_multiple_paragraphs(self):
        text = "word " * 100 + "\n\n" + "word " * 100
        result = get_read_duration(text)
        self.assertEqual(result, 2)

    def test_minimum_return_value(self):
        result = get_read_duration("a")
        self.assertEqual(result, 1)

    def test_large_input(self):
        words = "word " * 10000
        result = get_read_duration(words)
        self.assertEqual(result, 50)