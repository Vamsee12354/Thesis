from implementation_manual import slugify_manual
import unittest

class TestSlugifyManual(unittest.TestCase):

    def test_basic_slugification(self):
        self.assertEqual(slugify_manual("Hello, World!"), "hello-world")
        self.assertEqual(slugify_manual("foo bar"), "foo-bar")
        self.assertEqual(slugify_manual("  leading and trailing  "), "leading-and-trailing")

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
        self.assertEqual(slugify_manual("a b c", separator="."), "a.b.c")

    def test_case_handling(self):
        self.assertEqual(slugify_manual("StUdLy CaPs", lowercase=False), "StUdLy-CaPs")
        self.assertEqual(slugify_manual("StUdLy CaPs", lowercase=True), "studly-caps")
        self.assertEqual(slugify_manual("ALL CAPS", lowercase=False), "ALL-CAPS")

    def test_truncate_functionality(self):
        self.assertEqual(slugify_manual("Call me maybe", truncate=10), "call-me")
        self.assertEqual(slugify_manual("Call me maybe", truncate=5), "call")
        self.assertEqual(slugify_manual("Call me maybe", truncate=15), "call-me-maybe")
        self.assertEqual(slugify_manual("a b c d e", truncate=3), "a-b")

    def test_truncate_edge_cases(self):
        self.assertIsNone(slugify_manual("Hello", truncate=1))
        self.assertIsNone(slugify_manual("Hello", truncate=2))
        self.assertEqual(slugify_manual("Hello", truncate=5), "hello")
        self.assertEqual(slugify_manual("Hello", truncate=10), "hello")

    def test_ignore_functionality(self):
        self.assertEqual(slugify_manual("你好，世界", ignore=["你", "好"]), "你好-shi-jie")
        self.assertEqual(slugify_manual("foo!bar", ignore=["!"]), "foo!bar")
        self.assertEqual(slugify_manual("a@b#c", ignore=["@", "#"]), "a@b#c")
        self.assertEqual(slugify_manual("test@test.com", ignore=["@"]), "test@test.com")

    def test_ignore_with_list_input(self):
        self.assertEqual(slugify_manual("a!b@c#d", ignore=["!", "@"]), "a!b@c-d")
        self.assertEqual(slugify_manual("x*y+z", ignore=["*", "+"]), "x*y+z")

    def test_mixed_language_input(self):
        self.assertEqual(slugify_manual("こんにちは世界"), "konnichiha-shi-jie")
        self.assertEqual(slugify_manual("Привет мир"), "privet-mir")
        self.assertEqual(slugify_manual("안녕하세요 세계"), "annyeonghaseyo-segye")

    def test_whitespace_handling(self):
        self.assertEqual(slugify_manual("  multiple   spaces  "), "multiple-spaces")
        self.assertEqual(slugify_manual("\t tabs and \n newlines \r"), "tabs-and-newlines")

    def test_special_characters(self):
        self.assertEqual(slugify_manual("foo@bar#baz"), "foobarbaz")
        self.assertEqual(slugify_manual("foo-bar_baz"), "foo-bar-baz")
        self.assertEqual(slugify_manual("foo.bar,baz"), "foobarbaz")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            slugify_manual(123)
        with self.assertRaises(TypeError):
            slugify_manual(None)
        with self.assertRaises(TypeError):
            slugify_manual(["list", "input"])

    def test_ignore_with_empty_string(self):
        self.assertEqual(slugify_manual("test", ignore=""), "test")
        self.assertEqual(slugify_manual("test", ignore=[]), "test")

    def test_ignore_nonexistent_chars(self):
        self.assertEqual(slugify_manual("test", ignore=["x", "y"]), "test")

    def test_truncate_with_ignore(self):
        self.assertEqual(slugify_manual("hello world", truncate=8, ignore=["l"]), "hel-lo-w")
        self.assertEqual(slugify_manual("hello world", truncate=5, ignore=["l"]), "hel-lo")