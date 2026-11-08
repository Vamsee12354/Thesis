import unittest
from implementation_manual import slugify_manual

class TestSlugifyManual(unittest.TestCase):

    def test_basic_slugification(self):
        # Happy path: standard string
        self.assertEqual(slugify_manual("Hello, World!"), "hello-world")

    def test_custom_separator(self):
        # Happy path: custom separator (empty string)
        self.assertEqual(slugify_manual("Madam, I'm Adam", separator=""), "madamimadam")
        # Happy path: custom separator (underscore)
        self.assertEqual(slugify_manual("Hello World", separator="_"), "hello_world")

    def test_casing_options(self):
        # Happy path: disable lowercase
        self.assertEqual(slugify_manual("StUdLy CaPs", lowercase=False), "StUdLy-CaPs")
        # Default behavior is lowercase
        self.assertEqual(slugify_manual("UPPER"), "upper")

    def test_truncation(self):
        # Happy path: truncate without breaking words
        self.assertEqual(slugify_manual("Call me maybe", truncate=10), "call-me")
        # Edge case: truncate value smaller than first word
        self.assertEqual(slugify_manual("Hello World", truncate=2), None)
        # Edge case: truncate exactly at word boundary
        self.assertEqual(slugify_manual("Hello World", truncate=5), "hello")

    def test_ignore_characters(self):
        # Happy path: ignore specific characters (Unicode)
        # Note: The spec example "你好，世界" -> "你好-shi-jie" implies transliteration 
        # of the rest but preservation of ignored chars.
        self.assertEqual(slugify_manual("你好，世界", ignore=["你", "好"]), "你好-shi-jie")
        # Happy path: ignore punctuation
        self.assertEqual(slugify_manual("hello!world", ignore=["!"]), "hello!world")

    def test_unicode_transliteration(self):
        # Happy path: transliteration of non-ASCII
        # "你好" -> "ni-hao"
        self.assertEqual(slugify_manual("你好"), "ni-hao")

    def test_whitespace_handling(self):
        # Edge case: leading, trailing, and repeated whitespace
        self.assertEqual(slugify_manual("   foo    bar   "), "foo-bar")
        self.assertEqual(slugify_manual("\tnew\nline\r"), "new-line")

    def test_invalid_inputs_and_edge_cases(self):
        # Edge case: Empty input
        self.assertIsNone(slugify_manual(""))
        # Edge case: Input with only punctuation/invalid characters
        self.assertIsNone(slugify_manual("!!! @@@ ###"))
        # Edge case: Input that results in empty string after processing
        self.assertIsNone(slugify_manual("   "))

    def test_complex_combinations(self):
        # Combination of separator, lowercase, and truncation
        self.assertEqual(slugify_manual("  The Quick Brown Fox  ", separator="_", lowercase=True, truncate=12), "the_quick")
        # Combination of ignore and separator
        self.assertEqual(slugify_manual("A+B+C", ignore=["+"], separator="-"), "a+b+c")

if __name__ == '__main__':
    unittest.main()