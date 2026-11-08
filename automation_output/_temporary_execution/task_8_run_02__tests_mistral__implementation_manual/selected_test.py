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
        self.assertEqual(slugify_manual("Hello World", separator=""), "helloworld")
        self.assertEqual(slugify_manual("Hello World", separator="."), "hello.world")

    def test_lowercase_option(self):
        self.assertEqual(slugify_manual("StUdLy CaPs", lowercase=True), "studly-caps")
        self.assertEqual(slugify_manual("StUdLy CaPs", lowercase=False), "StUdLy-CaPs")

    def test_truncate_option(self):
        self.assertEqual(slugify_manual("Call me maybe", truncate=10), "call-me")
        self.assertEqual(slugify_manual("Call me maybe", truncate=5), "call")
        self.assertEqual(slugify_manual("Call me maybe", truncate=3), "ca")
        self.assertEqual(slugify_manual("Call me maybe", truncate=1), "")

    def test_ignore_option(self):
        self.assertEqual(slugify_manual("你好，世界", ignore=["你", "好"]), "你好-shi-jie")
        self.assertEqual(slugify_manual("Hello, World!", ignore=["!"]), "hello-world!")
        self.assertEqual(slugify_manual("Test@ing", ignore=["@", "ing"]), "test@ing")
        self.assertEqual(slugify_manual("Test@ing", ignore=["@"]), "testing")

    def test_mixed_language_input(self):
        self.assertEqual(slugify_manual("こんにちは世界"), "konnichiha-shi-jie")
        self.assertEqual(slugify_manual("Привет мир"), "privet-mir")
        self.assertEqual(slugify_manual("안녕하세요 세계"), "annyeonghaseyo-segye")

    def test_repeated_whitespace(self):
        self.assertEqual(slugify_manual("foo    bar"), "foo-bar")
        self.assertEqual(slugify_manual("  foo  bar  "), "foo-bar")

    def test_special_characters(self):
        self.assertEqual(slugify_manual("foo@bar#baz"), "foobarbaz")
        self.assertEqual(slugify_manual("foo@bar#baz", separator="_"), "foo_bar_baz")
        self.assertEqual(slugify_manual("foo@bar#baz", ignore=["@"]), "foo@barbaz")

    def test_truncate_with_ignore(self):
        self.assertEqual(slugify_manual("Hello world", truncate=5, ignore=["world"]), "hello")
        self.assertEqual(slugify_manual("Hello world", truncate=10, ignore=["world"]), "hello-world")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            slugify_manual(123)
        with self.assertRaises(TypeError):
            slugify_manual(None)

    def test_ignore_as_list_or_string(self):
        self.assertEqual(slugify_manual("Hello, World!", ignore="!"), "hello-world!")
        self.assertEqual(slugify_manual("Hello, World!", ignore=["!", ","]), "hello-world!")