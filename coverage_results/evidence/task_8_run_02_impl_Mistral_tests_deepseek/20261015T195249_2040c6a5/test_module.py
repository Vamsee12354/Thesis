from implementation_manual import slugify_manual
import unittest


class TestSlugifyManual(unittest.TestCase):
    def test_basic_conversion(self):
        self.assertEqual(slugify_manual("Hello World"), "hello-world")
        self.assertEqual(slugify_manual("foo bar baz"), "foo-bar-baz")

    def test_punctuation_removal(self):
        self.assertEqual(slugify_manual("Hello, World!"), "hello-world")
        self.assertEqual(slugify_manual("What's up?"), "whats-up")

    def test_custom_separator(self):
        self.assertEqual(slugify_manual("Hello World", separator="_"), "hello_world")
        self.assertEqual(slugify_manual("foo bar", separator=""), "foobar")

    def test_lowercase_parameter(self):
        self.assertEqual(slugify_manual("StUdLy CaPs", lowercase=False), "StUdLy-CaPs")
        self.assertEqual(slugify_manual("UPPER CASE", lowercase=True), "upper-case")

    def test_truncation(self):
        self.assertEqual(slugify_manual("Call me maybe", truncate=10), "call-me")
        self.assertEqual(slugify_manual("This is a long string", truncate=5), "this")

    def test_ignore_parameter(self):
        self.assertEqual(slugify_manual("你好，世界", ignore=["你","好"]), "你好-shi-jie")
        self.assertEqual(slugify_manual("$100 dollars", ignore=["$"]), "$100-dollars")

    def test_empty_input(self):
        self.assertIsNone(slugify_manual(""))
        self.assertIsNone(slugify_manual("   "))
        self.assertIsNone(slugify_manual("!@#$%"))

    def test_whitespace_handling(self):
        self.assertEqual(slugify_manual("  leading  trailing  "), "leading-trailing")
        self.assertEqual(slugify_manual("multiple    spaces"), "multiple-spaces")

    def test_unicode_transliteration(self):
        self.assertEqual(slugify_manual("Café"), "cafe")
        self.assertEqual(slugify_manual("München"), "munchen")

    def test_edge_case_truncation(self):
        self.assertEqual(slugify_manual("a b c", truncate=1), "a")
        self.assertIsNone(slugify_manual("a b c", truncate=0))

    def test_mixed_language_input(self):
        self.assertEqual(slugify_manual("Hello 你好"), "hello-ni-hao")
        self.assertEqual(slugify_manual("東京タワー"), "dong-jing-ta-wa")