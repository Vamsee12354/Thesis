from implementation_manual import slugify_manual
import unittest

class TestSlugifyManual(unittest.TestCase):
    def test_basic_slugification(self):
        self.assertEqual(slugify_manual("Hello, World!"), "hello-world")
        self.assertEqual(slugify_manual("foo bar"), "foo-bar")
        self.assertEqual(slugify_manual("  leading and trailing spaces  "), "leading-and-trailing-spaces")

    def test_empty_and_punctuation_only(self):
        self.assertIsNone(slugify_manual(""))
        self.assertIsNone(slugify_manual("!@#$%^&*()"))
        self.assertIsNone(slugify_manual("   "))

    def test_custom_separator(self):
        self.assertEqual(slugify_manual("Hello World", separator="_"), "hello_world")
        self.assertEqual(slugify_manual("foo bar", separator=""), "foobar")
        self.assertEqual(slugify_manual("foo bar", separator="."), "foo.bar")

    def test_case_handling(self):
        self.assertEqual(slugify_manual("StUdLy CaPs", lowercase=False), "StUdLy-CaPs")
        self.assertEqual(slugify_manual("StUdLy CaPs", lowercase=True), "studly-caps")
        self.assertEqual(slugify_manual("ALL CAPS", lowercase=False), "ALL-CAPS")

    def test_truncate_functionality(self):
        self.assertEqual(slugify_manual("Call me maybe", truncate=10), "call-me")
        self.assertEqual(slugify_manual("Call me maybe", truncate=5), "call")
        self.assertEqual(slugify_manual("Call me maybe", truncate=3), "call")
        self.assertEqual(slugify_manual("Short", truncate=100), "short")

    def test_ignore_functionality(self):
        self.assertEqual(slugify_manual("你好，世界", ignore=["你", "好"]), "你好-shi-jie")
        self.assertEqual(slugify_manual("foo!bar", ignore=["!"]), "foo!bar")
        self.assertEqual(slugify_manual("a!b@c#d", ignore=["!", "@"]), "a!b@c-d")

    def test_mixed_language_input(self):
        self.assertEqual(slugify_manual("こんにちは世界"), "konnichiha-shi-jie")
        self.assertEqual(slugify_manual("Привет мир"), "privet-mir")
        self.assertEqual(slugify_manual("안녕하세요 세계"), "annyeonghaseyo-segye")

    def test_repeated_whitespace(self):
        self.assertEqual(slugify_manual("foo    bar"), "foo-bar")
        self.assertEqual(slugify_manual("  multiple   spaces  "), "multiple-spaces")

    def test_special_characters(self):
        self.assertEqual(slugify_manual("foo@bar#baz$"), "foo-bar-baz")
        self.assertEqual(slugify_manual("foo.bar,baz"), "foo-bar-baz")
        self.assertEqual(slugify_manual("foo/bar\\baz"), "foo-bar-baz")

    def test_truncate_edge_cases(self):
        self.assertEqual(slugify_manual("hello world", truncate=1), "")
        self.assertEqual(slugify_manual("hello world", truncate=2), "")
        self.assertEqual(slugify_manual("a b c", truncate=1), "")
        self.assertEqual(slugify_manual("a b c", truncate=2), "a")

    def test_ignore_with_truncate(self):
        self.assertEqual(slugify_manual("foo!bar!baz", ignore=["!"], truncate=5), "foo!b")
        self.assertEqual(slugify_manual("foo!bar!baz", ignore=["!"], truncate=3), "foo")

    def test_non_string_input_handling(self):
        with self.assertRaises(TypeError):
            slugify_manual(123)
        with self.assertRaises(TypeError):
            slugify_manual(None)
        with self.assertRaises(TypeError):
            slugify_manual(["list", "input"])