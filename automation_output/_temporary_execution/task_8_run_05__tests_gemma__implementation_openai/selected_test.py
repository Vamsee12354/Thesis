import unittest
from implementation_manual import slugify_manual

class TestSlugifyManual(unittest.TestCase):

    def test_basic_slugification(self):
        # Happy path: standard string
        self.assertEqual(slugify_manual("Hello World"), "hello-world")

    def test_separator_customization(self):
        # Custom separator
        self.assertEqual(slugify_manual("Hello World", separator="_"), "hello_world")
        # Empty separator
        self.assertEqual(slugify_manual("Madam, I'm Adam", separator=""), "madamimadam")

    def test_lowercase_option(self):
        # Default lowercase is True
        self.assertEqual(slugify_manual("StUdLy CaPs"), "studly-caps")
        # Disable lowercase
        self.assertEqual(slugify_manual("StUdLy CaPs", lowercase=False), "StUdLy-CaPs")

    def test_ignore_characters(self):
        # Ignore specific characters (list)
        self.assertEqual(slugify_manual("你好，世界", ignore=["你", "好"]), "你好-shi-jie")
        # Ignore specific characters (string)
        self.assertEqual(slugify_manual("Price: $100", ignore="$"), "price-$100")

    def test_truncation(self):
        # Truncate without breaking words
        self.assertEqual(slugify_manual("Call me maybe", truncate=10), "call-me")
        # Truncate very small value
        self.assertEqual(slugify_manual("abc def", truncate=2), None)

    def test_punctuation_and_whitespace_cleanup(self):
        # Leading/trailing/repeated whitespace and punctuation
        self.assertEqual(slugify_manual("  Hello , World !  "), "hello-world")
        self.assertEqual(slugify_manual("foo...bar---baz"), "foo-bar-baz")

    def test_unicode_transliteration(self):
        # Transliteration of non-ASCII characters
        self.assertEqual(slugify_manual("你好"), "ni-hao")

    def test_invalid_inputs_and_edge_cases(self):
        # Empty input
        self.assertIsNone(slugify_manual(""))
        # Input with only punctuation/invalid characters
        self.assertIsNone(slugify_manual("!!! ???"))
        # Input that becomes empty after processing
        self.assertIsNone(slugify_manual("   "))

    def test_complex_combination(self):
        # Combination of multiple parameters
        # "Hello, World!" -> "hello-world" -> truncate 8 -> "hello"
        self.assertEqual(slugify_manual("Hello, World!", truncate=8), "hello")

if __name__ == '__main__':
    unittest.main()