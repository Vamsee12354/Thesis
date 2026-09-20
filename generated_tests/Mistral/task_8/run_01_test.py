from implementation_manual import slugify_manual
import unittest

class TestSlugifyManual(unittest.TestCase):

    def test_basic_slugification(self):
        self.assertEqual(slugify_manual("Hello, World!"), "hello-world")
        self.assertEqual(slugify_manual("foo bar"), "foo-bar")

    def test_empty_input(self):
        self.assertIsNone(slugify_manual(""))
        self.assertIsNone(slugify_manual("   "))

    def test_punctuation_only(self):
        self.assertIsNone(slugify_manual("!@#$%^&*()"))
        self.assertIsNone(slugify_manual(".,?!"))

    def test_custom_separator(self):
        self.assertEqual(slugify_manual("Hello World", separator="_"), "hello_world")
        self.assertEqual(slugify_manual("foo bar", separator=""), "foobar")

    def test_lowercase_conversion(self):
        self.assertEqual(slugify_manual("StUdLy CaPs", lowercase=True), "studly-caps")
        self.assertEqual(slugify_manual("StUdLy CaPs", lowercase=False), "StUdLy-CaPs")

    def test_ignore_characters(self):
        self.assertEqual(
            slugify_manual("你好，世界", ignore=["你好"]),
            "你好-shi-jie"
        )
        self.assertEqual(
            slugify_manual("Call me maybe", ignore=["me"]),
            "call-me-maybe"
        )

    def test_truncate_length(self):
        self.assertEqual(slugify_manual("Call me maybe", truncate=10), "call-me")
        self.assertEqual(slugify_manual("Hello world", truncate=5), "hello")
        self.assertEqual(slugify_manual("Short", truncate=100), "short")

    def test_whitespace_handling(self):
        self.assertEqual(slugify_manual("  foo   bar  "), "foo-bar")
        self.assertEqual(slugify_manual("foo\tbar\nbaz"), "foo-bar-baz")

    def test_non_ascii_transliteration(self):
        self.assertEqual(slugify_manual("こんにちは世界"), "konnichiha-shijie")
        self.assertEqual(slugify_manual("Привет мир"), "privet-mir")

    def test_invalid_truncate(self):
        self.assertEqual(slugify_manual("Hello world", truncate=0), "")
        self.assertEqual(slugify_manual("Hello world", truncate=-1), "")

    def test_preserve_ignore_with_separator(self):
        self.assertEqual(
            slugify_manual("foo bar baz", ignore=["bar"], separator="."),
            "foo.bar.baz"
        )

    def test_no_valid_words_after_cleanup(self):
        self.assertIsNone(slugify_manual("!@#$%^"))
        self.assertIsNone(slugify_manual("12345", lowercase=False))

    def test_mixed_language_with_ignore(self):
        self.assertEqual(
            slugify_manual("你好，世界", ignore=["你好"]),
            "你好-shi-jie"
        )
        self.assertEqual(
            slugify_manual("こんにちは、世界", ignore=["こんにちは"]),
            "こんにちは-shi-jie"
        )