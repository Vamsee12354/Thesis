import unittest
from implementation_manual import get_read_duration

class TestGetReadDuration(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(get_read_duration(""), 1)

    def test_single_word(self):
        self.assertEqual(get_read_duration("word"), 1)

    def test_normal_paragraph(self):
        self.assertEqual(get_read_duration("This is a simple blog post with about fifty words total..."), 1)

    def test_long_post(self):
        long_post = " ".join(["word"] * 450)
        self.assertEqual(get_read_duration(long_post), 3)

    def test_excessive_whitespace(self):
        self.assertEqual(get_read_duration("   "), 1)

    def test_non_latin_characters(self):
        non_latin_text = "这是一个简单的博客文章，包含大约五十个词。"
        self.assertEqual(get_read_duration(non_latin_text), 1)

    def test_minimum_return_value(self):
        self.assertEqual(get_read_duration("a"), 1)

if __name__ == '__main__':
    unittest.main()
