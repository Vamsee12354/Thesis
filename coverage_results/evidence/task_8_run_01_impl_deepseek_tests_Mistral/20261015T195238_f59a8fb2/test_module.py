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

    def test_case_handling(self):
        self.assertEqual(slugify_manual("StUdLy CaPs", lowercase=False), "StUdLy-CaPs")
        self.assertEqual(slugify_manual("StUdLy CaPs"), "studly-caps")
        self.assertEqual(slugify_manual("ALL CAPS"), "all-caps")

    def test_truncate_functionality(self):
        self.assertEqual(slugify_manual("Call me maybe", truncate=10), "call-me")
        self.assertEqual(slugify_manual("Call me maybe", truncate=5), "call")
        self.assertEqual(slugify_manual("Call me maybe", truncate=3), "call")
        self.assertEqual(slugify_manual("Call me maybe", truncate=1), "")

    def test_ignore_functionality(self):
        self.assertEqual(slugify_manual("你好，世界", ignore=["你", "好"]), "你好-shi-jie")
        self.assertEqual(slugify_manual("foo!bar", ignore=["!"]), "foo!bar")
        self.assertEqual(slugify_manual("foo!bar", ignore=["!"]), "foo!bar")
        self.assertEqual(slugify_manual("a!b@c#d", ignore=["!", "@"]), "a!b@c-d")

    def test_ignore_with_list_input(self):
        self.assertEqual(slugify_manual("test@ing#now", ignore=["@", "#"]), "test@ing#now")
        self.assertEqual(slugify_manual("test@ing#now", ignore="@"), "test@ing-now")

    def test_mixed_language_input(self):
        self.assertEqual(slugify_manual("こんにちは世界"), "konnichiha-shi-jie")
        self.assertEqual(slugify_manual("123 456"), "123-456")
        self.assertEqual(slugify_manual("café au lait"), "cafe-au-lait")

    def test_numeric_input(self):
        self.assertEqual(slugify_manual("123 456"), "123-456")
        self.assertEqual(slugify_manual("123"), "123")
        self.assertIsNone(slugify_manual("!@#123"))

    def test_special_characters(self):
        self.assertEqual(slugify_manual("foo@bar#baz"), "foo-bar-baz")
        self.assertEqual(slugify_manual("foo bar\tbaz"), "foo-bar-baz")
        self.assertEqual(slugify_manual("foo\nbar baz"), "foo-bar-baz")

    def test_truncate_with_ignore(self):
        self.assertEqual(slugify_manual("foo bar baz", truncate=5, ignore=["foo"]), "foo")
        self.assertEqual(slugify_manual("foo bar baz", truncate=7, ignore=["foo"]), "foo-bar")

    def test_invalid_truncate_values(self):
        self.assertEqual(slugify_manual("foo bar", truncate=0), "")
        self.assertEqual(slugify_manual("foo bar", truncate=-1), "")

    def test_whitespace_handling(self):
        self.assertEqual(slugify_manual("  leading and trailing  "), "leading-and-trailing")
        self.assertEqual(slugify_manual("multiple   spaces"), "multiple-spaces")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            slugify_manual(123)
        with self.assertRaises(TypeError):
            slugify_manual(None)