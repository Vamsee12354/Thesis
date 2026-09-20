from implementation_manual import slugify_manual
import unittest

class TestSlugifyManual(unittest.TestCase):

    def test_basic_slugification(self):
        self.assertEqual(slugify_manual("Hello, World!"), "hello-world")
        self.assertEqual(slugify_manual(" foo bar "), "foo-bar")
        self.assertEqual(slugify_manual("Madam, I'm Adam"), "madam-im-adam")

    def test_custom_separator(self):
        self.assertEqual(slugify_manual("Hello World", separator="_"), "hello_world")
        self.assertEqual(slugify_manual("Hello World", separator=""), "helloworld")
        self.assertEqual(slugify_manual("Hello World", separator="."), "hello.world")

    def test_case_handling(self):
        self.assertEqual(slugify_manual("StUdLy CaPs", lowercase=False), "StUdLy-CaPs")
        self.assertEqual(slugify_manual("StUdLy CaPs", lowercase=True), "studly-caps")
        self.assertEqual(slugify_manual("StUdLy CaPs"), "studly-caps")

    def test_truncation(self):
        self.assertEqual(slugify_manual("Call me maybe", truncate=10), "call-me")
        self.assertEqual(slugify_manual("Call me maybe", truncate=5), "call")
        self.assertEqual(slugify_manual("Call me maybe", truncate=1), "")
        self.assertEqual(slugify_manual("Hello world", truncate=100), "hello-world")

    def test_ignore_characters(self):
        self.assertEqual(
            slugify_manual("你好，世界", ignore=["你好"]),
            "你好-世界"
        )
        self.assertEqual(
            slugify_manual("Hello, World!", ignore=["!"]),
            "hello-world!"
        )
        self.assertEqual(
            slugify_manual("Test@123", ignore=["@"]),
            "test@123"
        )

    def test_unicode_transliteration(self):
        self.assertEqual(slugify_manual("你好世界"), "ni-hao-shi-jie")
        self.assertEqual(slugify_manual("こんにちは世界"), "konnichiha-shi-jie")
        self.assertEqual(
            slugify_manual("你好，世界", ignore=["你好"]),
            "你好-shi-jie"
        )

    def test_edge_cases(self):
        self.assertIsNone(slugify_manual(""))
        self.assertIsNone(slugify_manual("!@#$%^&*()"))
        self.assertIsNone(slugify_manual("   "))
        self.assertEqual(slugify_manual("a", truncate=1), "a")
        self.assertEqual(slugify_manual("a b", truncate=1), "a")

    def test_whitespace_cleanup(self):
        self.assertEqual(slugify_manual("  multiple   spaces  "), "multiple-spaces")
        self.assertEqual(slugify_manual("\t tabs \n and \r\n newlines"), "tabs-and-newlines")

    def test_punctuation_handling(self):
        self.assertEqual(slugify_manual("Hello... World!!!"), "hello-world")
        self.assertEqual(slugify_manual("Price: $100"), "price-100")
        self.assertEqual(slugify_manual("Email: test@example.com"), "email-testexamplecom")

    def test_preserve_ignore_with_separator(self):
        self.assertEqual(
            slugify_manual("Test@123", separator="_", ignore=["@"]),
            "test_@_123"
        )
        self.assertEqual(
            slugify_manual("Hello World", separator="", ignore=["Hello"]),
            "HelloWorld"
        )