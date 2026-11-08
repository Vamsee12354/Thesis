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

    def test_uppercase_output(self):
        self.assertEqual(slugify_manual("StUdLy CaPs", lowercase=False), "StUdLy-CaPs")

    def test_truncation(self):
        self.assertEqual(slugify_manual("Call me maybe", truncate=10), "call-me")

    def test_ignore_characters(self):
        self.assertEqual(slugify_manual("你好，世界", ignore=["你", "好"]), "你好-shi-jie")

    def test_leading_trailing_whitespace(self):
        self.assertEqual(slugify_manual("  foo bar  "), "foo-bar")

    def test_repeated_whitespace(self):
        self.assertEqual(slugify_manual("foo    bar"), "foo-bar")

    def test_mixed_language_input(self):
        self.assertEqual(slugify_manual("你好，世界"), "ni-hao-shi-jie")

    def test_truncate_too_small(self):
        self.assertIsNone(slugify_manual("foo bar", truncate=1))

    def test_ignore_characters_not_in_input(self):
        self.assertEqual(slugify_manual("hello world", ignore=["x", "y"]), "hello-world")

    def test_truncate_exact_length(self):
        self.assertEqual(slugify_manual("hello world", truncate=11), "hello-world")

    def test_truncate_longer_than_input(self):
        self.assertEqual(slugify_manual("hello world", truncate=20), "hello-world")

    def test_non_ascii_characters(self):
        self.assertEqual(slugify_manual("Café au lait"), "cafe-au-lait")

    def test_ignore_characters_with_separator(self):
        self.assertEqual(slugify_manual("hello-world", ignore=["-"]), "hello-world")

    def test_truncate_with_ignore_characters(self):
        self.assertEqual(slugify_manual("hello-world", truncate=5, ignore=["-"]), "hello")

    def test_truncate_with_ignore_characters_no_match(self):
        self.assertEqual(slugify_manual("hello world", truncate=5, ignore=["x"]), "hello")

    def test_truncate_with_ignore_characters_exact_match(self):
        self.assertEqual(slugify_manual("hello-world", truncate=11, ignore=["-"]), "hello-world")

    def test_truncate_with_ignore_characters_longer_than_input(self):
        self.assertEqual(slugify_manual("hello-world", truncate=20, ignore=["-"]), "hello-world")