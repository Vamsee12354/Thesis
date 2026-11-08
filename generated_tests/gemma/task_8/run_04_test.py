import unittest
from implementation_manual import slugify_manual

class TestSlugifyManual(unittest.TestCase):

    def test_basic_slugification(self):
        # Happy path: standard string
        self.assertEqual(slugify_manual("Hello World"), "hello-world")
        # Happy path: multiple spaces and punctuation
        self.assertEqual(slugify_manual(" Hello, World!"), "hello-world")

    def test_separator_customization(self):
        # Custom separator (empty string)
        self.assertEqual(slugify_manual("Madam, I'm Adam", separator=""), "madamimadam")
        # Custom separator (underscore)
        self.assertEqual(slugify_manual("Hello World", separator="_"), "hello_world")

    def test_casing_customization(self):
        # Lowercase default (True)
        self.assertEqual(slugify_manual("StUdLy CaPs"), "studly-caps")
        # Uppercase preservation (lowercase=False)
        self.assertEqual(slugify_manual("StUdLy CaPs", lowercase=False), "StUdLy-CaPs")

    def test_ignore_parameter(self):
        # Ignore specific characters (list)
        # Note: Based on example "你好，世界 " with ignore ["你","好"] -> "你好-shi-jie"
        # This implies '你' and '好' are preserved and not transliterated/removed
        self.assertEqual(slugify_manual("你好，世界", ignore=["你", "好"]), "你好-shi-jie")
        # Ignore specific characters (string)
        self.assertEqual(slugify_manual("a!b@c", ignore="!@"), "a-b-c")

    def test_truncation(self):
        # Truncate without breaking words
        self.assertEqual(slugify_manual("Call me maybe", truncate=10), "call-me")
        # Truncate very small
        self.assertEqual(slugify_manual("Hello World", truncate=1), None)
        # Truncate exactly at word boundary
        self.assertEqual(slugify_manual("Hello World", truncate=5), "hello")

    def test_unicode_transliteration(self):
        # Transliteration of Chinese characters
        # Based on example: "你好" -> "ni-hao"
        self.assertEqual(slugify_manual("你好"), "ni-hao")

    def test_edge_cases_and_invalid_inputs(self):
        # Empty input
        self.assertIsNone(slugify_manual(""))
        # Input with only punctuation/whitespace
        self.assertIsNone(slugify_manual("!!!???"))
        self.assertIsNone(slugify_manual("   "))
        # Input with only ignored characters that are not alphanumeric
        # If the result contains no alphanumeric and no separator, it should return None
        self.assertIsNone(slugify_manual("!!!", ignore="!"))

    def test_whitespace_handling(self):
        # Leading, trailing, and repeated whitespace
        self.assertEqual(slugify_manual("  multiple   spaces  "), "multiple-spaces")

if __name__ == '__main__':
    unittest.main()