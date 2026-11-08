from implementation_manual import slugify_manual
import unittest

class TestSlugifyManual(unittest.TestCase):

    def test_basic_slugification(self):
        self.assertEqual(slugify_manual("Hello, World!"), "hello-world")
        self.assertEqual(slugify_manual("foo bar"), "foo-bar")
        self.assertEqual(slugify_manual("  foo   bar  "), "foo-bar")

    def test_empty_input(self):
        self.assertIsNone(slugify_manual(""))
        self.assertIsNone(slugify_manual("   "))
        self.assertIsNone(slugify_manual("!@#$%^&*()"))

    def test_punctuation_only(self):
        self.assertIsNone(slugify_manual("!@#$%^&*()"))
        self.assertIsNone(slugify_manual(".,?!"))

    def test_custom_separator(self):
        self.assertEqual(slugify_manual("Hello World", separator="_"), "hello_world")
        self.assertEqual(slugify_manual("foo bar", separator=""), "foobar")
        self.assertEqual(slugify_manual("foo bar", separator="."), "foo.bar")

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
        self.assertEqual(slugify_manual("foo!bar", ignore=["!"]), "foo!bar")
        self.assertEqual(slugify_manual("foo!bar", ignore=["!"]), "foo!bar")
        self.assertEqual(slugify_manual("foo bar", ignore=[" "]), "foo bar")

    def test_ignore_as_list(self):
        self.assertEqual(slugify_manual("foo!bar", ignore=["!", "@"]), "foo!bar")
        self.assertEqual(slugify_manual("foo@bar", ignore=["!", "@"]), "foo@bar")

    def test_ignore_as_string(self):
        self.assertEqual(slugify_manual("foo!bar", ignore="!"), "foo!bar")
        self.assertEqual(slugify_manual("foo@bar", ignore="@"), "foo@bar")

    def test_mixed_language_input(self):
        self.assertEqual(slugify_manual("你好世界"), "ni-hao-shi-jie")
        self.assertEqual(slugify_manual("こんにちは世界"), "konnichiha-shi-jie")
        self.assertEqual(slugify_manual("안녕하세요 세계"), "annyeonghaseyo-segye")

    def test_preserve_ignore_chars(self):
        self.assertEqual(slugify_manual("foo@bar", ignore="@"), "foo@bar")
        self.assertEqual(slugify_manual("foo bar", ignore=" "), "foo bar")
        self.assertEqual(slugify_manual("foo-bar", ignore="-"), "foo-bar")

    def test_truncate_with_ignore(self):
        self.assertEqual(slugify_manual("foo bar baz", truncate=5, ignore=[" "]), "foo b")
        self.assertEqual(slugify_manual("foo!bar!baz", truncate=5, ignore=["!"]), "foo!b")

    def test_non_utf8_input(self):
        with self.assertRaises(UnicodeError):
            slugify_manual("invalid \x80 utf8")

    def test_custom_separator_with_ignore(self):
        self.assertEqual(slugify_manual("foo bar", separator="_", ignore=[" "]), "foo bar")
        self.assertEqual(slugify_manual("foo bar", separator="_", ignore=[" "]), "foo bar")

    def test_truncate_edge_cases(self):
        self.assertEqual(slugify_manual("a b c", truncate=1), "")
        self.assertEqual(slugify_manual("a b c", truncate=2), "a")
        self.assertEqual(slugify_manual("a b c", truncate=3), "a-b")
        self.assertEqual(slugify_manual("a b c", truncate=4), "a-b")

    def test_ignore_with_punctuation(self):
        self.assertEqual(slugify_manual("foo!bar", ignore=["!"]), "foo!bar")
        self.assertEqual(slugify_manual("foo!bar!", ignore=["!"]), "foo!bar!")

    def test_whitespace_cleanup(self):
        self.assertEqual(slugify_manual("  foo   bar  "), "foo-bar")
        self.assertEqual(slugify_manual("\tfoo\nbar\r\nbaz"), "foo-bar-baz")