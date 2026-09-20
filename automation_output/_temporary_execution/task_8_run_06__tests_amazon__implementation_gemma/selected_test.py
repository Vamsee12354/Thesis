import unittest
from implementation_manual import slugify_manual

class TestSlugifyManual(unittest.TestCase):

    def test_basic_slugification(self):
        self.assertEqual(slugify_manual(" Hello, World!"), "hello-world")

    def test_empty_input(self):
        self.assertIsNone(slugify_manual(""))

    def test_punctuation_only_input(self):
        self.assertIsNone(slugify_manual(",!?"))

    def test_separator_empty_string(self):
        self.assertEqual(slugify_manual("Madam, I’m Adam", separator=""), "madamimadam")

    def test_lowercase_false(self):
        self.assertEqual(slugify_manual(" StUdLy CaPs ", lowercase=False), "StUdLy-CaPs")

    def test_truncate_value(self):
        self.assertEqual(slugify_manual("Call me maybe", truncate=10), "call-me")

    def test_ignore_characters(self):
        self.assertEqual(slugify_manual("\u4f60 \u597d \uff0c \u4e16 \u754c", ignore=["\u4f60 "," \u597d "]), "\u4f60\u597d-shi-jie")

    def test_leading_trailing_whitespace(self):
        self.assertEqual(slugify_manual(" foo bar "), "foo-bar")

    def test_repeated_whitespace(self):
        self.assertEqual(slugify_manual("foo   bar"), "foo-bar")

    def test_mixed_language_input(self):
        self.assertEqual(slugify_manual("\u4f60 \u597d"), "ni-hao")

    def test_very_small_truncate_value(self):
        self.assertIsNone(slugify_manual("a", truncate=1))

if __name__ == '__main__':
    unittest.main()
