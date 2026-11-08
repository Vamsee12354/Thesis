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
        self.assertEqual(slugify_manual("test@ing", ignore="@"), "test@ing")

    def test_ignore_with_list_input(self):
        self.assertEqual(slugify_manual("a!b@c#d", ignore=["!", "@"]), "a!b@c-d")
        self.assertEqual(slugify_manual("x*y+z", ignore=["*", "+"]), "x*y-z")

    def test_mixed_language_transliteration(self):
        self.assertEqual(slugify_manual("こんにちは世界"), "konnichiha-shijie")
        self.assertEqual(slugify_manual("Привет мир"), "privet-mir")
        self.assertEqual(slugify_manual("안녕하세요 세계"), "annyeonghaseyo-segye")

    def test_ignore_with_transliteration(self):
        self.assertEqual(slugify_manual("你好，世界", ignore=["世"]), "ni-hao-世")
        self.assertEqual(slugify_manual("こんにちは世界", ignore=["世"]), "konnichiha-世")

    def test_repeated_whitespace(self):
        self.assertEqual(slugify_manual("foo    bar"), "foo-bar")
        self.assertEqual(slugify_manual("  multiple   spaces  "), "multiple-spaces")

    def test_non_alphanumeric_preservation(self):
        self.assertEqual(slugify_manual("foo@bar#baz", ignore=["@", "#"]), "foo@bar#baz")
        self.assertEqual(slugify_manual("a$b%c^d", ignore=["$", "%"]), "a$b%c-d")

    def test_default_parameters(self):
        self.assertEqual(slugify_manual("Hello World"), "hello-world")
        self.assertEqual(slugify_manual("Test", separator="-", lowercase=True), "test")
        self.assertEqual(slugify_manual("Test", separator="_", lowercase=False), "Test")

    def test_invalid_truncate_values(self):
        with self.assertRaises(ValueError):
            slugify_manual("Hello", truncate=0)
        with self.assertRaises(ValueError):
            slugify_manual("Hello", truncate=-1)
        with self.assertRaises(TypeError):
            slugify_manual("Hello", truncate="invalid")