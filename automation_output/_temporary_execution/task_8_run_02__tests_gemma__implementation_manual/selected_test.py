import unittest
from implementation_manual import slugify_manual

class TestSlugifyManual(unittest.TestCase):

    def test_basic_slugification(self):
        # Happy path: standard string with punctuation
        # Expected: "hello-world" (assuming default separator is ' - ')
        # Note: The spec example shows " hello - world " with spaces around the dash.
        # We follow the example's exact output format.
        result = slugify_manual(" Hello , World !")
        self.assertEqual(result, " hello - world ")

    def test_custom_separator(self):
        # Happy path: custom separator (empty string)
        result = slugify_manual(" Madam , I'm Adam ", separator="")
        self.assertEqual(result, "madamimadam")

    def test_case_sensitivity(self):
        # Happy path: disable lowercase
        result = slugify_manual(" StUdLy CaPs ", lowercase=False)
        self.assertEqual(result, " StUdLy - CaPs ")

    def test_truncation(self):
        # Happy path: truncate without breaking words
        # "call-me-maybe" -> "call-me" (10 chars limit)
        result = slugify_manual(" Call me maybe ", truncate=10)
        self.assertEqual(result, " call - me ")

    def test_ignore_characters(self):
        # Happy path: preserve specific characters
        # Input: "\u4f60 \u597d \uff0c \u4e16 \u754c"
        # Ignore: ["\u4f60", "\u597d"]
        # Expected: "\u4f60 \u597d - shi - jie" (based on spec example)
        text = "\u4f60 \u597d \uff0c \u4e16 \u754c"
        ignore_list = ["\u4f60", "\u597d"]
        result = slugify_manual(text, ignore=ignore_list)
        self.assertEqual(result, "\u4f60 \u597d - shi - jie ")

    def test_empty_input(self):
        # Edge case: empty string
        self.assertIsNone(slugify_manual(""))

    def test_only_punctuation_input(self):
        # Edge case: input contains only invalid characters/punctuation
        self.assertIsNone(slugify_manual("!!! @@@ ###"))

    def test_small_truncate_value(self):
        # Edge case: very small truncate value that eliminates words
        # If truncate is 1, and words are longer, it might return None or empty
        result = slugify_manual(" Hello ", truncate=1)
        # Based on spec: "may eliminate all words if none fit" -> returns None
        self.assertIsNone(result)

    def test_whitespace_handling(self):
        # Edge case: leading, trailing, and repeated whitespace
        result = slugify_manual("   foo    bar   ")
        self.assertEqual(result, " foo - bar ")

    def test_unicode_transliteration(self):
        # Happy path: mixed language input
        # "\u4f60 \u597d" -> "ni - hao"
        result = slugify_manual("\u4f60 \u597d")
        self.assertEqual(result, "ni - hao")

    def test_ignore_as_string(self):
        # Happy path: ignore parameter as a single string
        result = slugify_manual("Hello! World", ignore="!")
        self.assertEqual(result, "hello! - world")

if __name__ == '__main__':
    unittest.main()