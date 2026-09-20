import unittest
from implementation_manual import get_read_duration

class TestGetReadDuration(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(get_read_duration(""), 1)

    def test_whitespace_only(self):
        self.assertEqual(get_read_duration("   "), 1)

    def test_single_word(self):
        self.assertEqual(get_read_duration("word"), 1)

    def test_short_post(self):
        self.assertEqual(get_read_duration("This is a short post"), 1)

    def test_exactly_200_words(self):
        text = "word " * 200
        self.assertEqual(get_read_duration(text), 1)

    def test_201_words(self):
        text = "word " * 201
        self.assertEqual(get_read_duration(text), 2)

    def test_450_words(self):
        text = "word " * 450
        self.assertEqual(get_read_duration(text), 3)

    def test_non_latin_chars(self):
        text = "中文 测试 文字"
        self.assertEqual(get_read_duration(text), 1)

    def test_mixed_chars(self):
        text = "中文 test 混合"
        self.assertEqual(get_read_duration(text), 1)

    def test_multiple_spaces_between_words(self):
        text = "word    word    word"
        self.assertEqual(get_read_duration(text), 1)