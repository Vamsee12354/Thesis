import unittest
from implementation_manual import get_read_duration

class TestGetReadDuration(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(get_read_duration(""), 1)

    def test_excessive_whitespace(self):
        self.assertEqual(get_read_duration("   "), 1)

    def test_short_text(self):
        self.assertEqual(get_read_duration("This is a short text."), 1)

    def test_normal_paragraph(self):
        text = "This is a simple blog post with about fifty words total ..."
        self.assertEqual(get_read_duration(text), 1)

    def test_long_post(self):
        text = "word " * 450
        self.assertEqual(get_read_duration(text), 3)

    def test_non_latin_characters(self):
        text = "这是一个测试"
        self.assertEqual(get_read_duration(text), 1)

    def test_exact_word_count(self):
        text = "word " * 200
        self.assertEqual(get_read_duration(text), 1)

    def test_word_count_just_above_threshold(self):
        text = "word " * 201
        self.assertEqual(get_read_duration(text), 2)

    def test_word_count_just_below_threshold(self):
        text = "word " * 199
        self.assertEqual(get_read_duration(text), 1)

    def test_multiple_spaces_between_words(self):
        text = "word    word    word"
        self.assertEqual(get_read_duration(text), 1)

    def test_newlines_in_text(self):
        text = "word\nword\nword"
        self.assertEqual(get_read_duration(text), 1)

    def test_tabs_in_text(self):
        text = "word\tword\tword"
        self.assertEqual(get_read_duration(text), 1)

    def test_mixed_whitespace(self):
        text = "word \t\nword \t\nword"
        self.assertEqual(get_read_duration(text), 1)

    def test_large_text(self):
        text = "word " * 1000
        self.assertEqual(get_read_duration(text), 5)

    def test_minimum_return_value(self):
        text = "a"
        self.assertEqual(get_read_duration(text), 1)

if __name__ == '__main__':
    unittest.main()