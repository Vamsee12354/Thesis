import unittest
from implementation_manual import slugify_manual

class TestSlugifyManual(unittest.TestCase):
    def test_basic_slug(self):
        self.assertEqual(slugify_manual("Hello, World!"), "hello-world")

    def test_empty_input(self):
        self.assertIsNone(slugify_manual(""))

    def test_punctuation_only(self):
        self.assertIsNone(slugify_manual("!@#$%^&*()"))

    def test_custom_separator(self):
        self.assertEqual(slugify_manual("Madam, I'm Adam", separator=""), "madamimadam")

    def test_lowercase_false(self):
        self.assertEqual(slugify_manual("StUdLy CaPs", lowercase=False), "StUdLy-CaPs")

    def test_truncate(self):
        self.assertEqual(slugify_manual("Call me maybe", truncate=10), "call-me")

    def test_ignore_characters(self):
        self.assertEqual(slugify_manual("你好，世界", ignore=["你", "好"]), "你好-shi-jie")

    def test_leading_trailing_whitespace(self):
        self.assertEqual(slugify_manual("  foo bar  "), "foo-bar")

    def test_repeated_whitespace(self):
        self.assertEqual(slugify_manual("foo   bar"), "foo-bar")

    def test_mixed_language_input(self):
        self.assertEqual(slugify_manual("你好，世界"), "ni-hao-shi-jie")

    def test_truncate_small_value(self):
        self.assertEqual(slugify_manual("foo bar", truncate=1), "foo")

    def test_truncate_eliminates_all_words(self):
        self.assertIsNone(slugify_manual("foo bar", truncate=0))

    def test_ignore_characters_not_in_input(self):
        self.assertEqual(slugify_manual("Hello, World!", ignore=["x", "y"]), "hello-world")

    def test_ignore_characters_preserve_case(self):
        self.assertEqual(slugify_manual("StUdLy CaPs", ignore=["S", "C"], lowercase=False), "StUdLy-CaPs")

    def test_truncate_with_ignore(self):
        self.assertEqual(slugify_manual("你好，世界", ignore=["你", "好"], truncate=5), "你好-shi")