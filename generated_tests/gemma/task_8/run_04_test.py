import unittest
from implementation_manual import slugify_manual

class TestSlugifyManual(unittest.TestCase):

    def test_basic_slugification(self):
        # Happy path: standard string with punctuation
        result = slugify_manual(" Hello , World !")
        self.assertEqual(result, "hello - world")

    def test_custom_separator(self):
        # Happy path: custom separator (empty string)
        result = slugify_manual(" Madam , I'm Adam ", separator="")
        self.assertEqual(result, "madamimadam")

    def test_case_sensitivity(self):
        # Happy path: disable lowercase
        result = slugify_manual(" StUdLy CaPs ", lowercase=False)
        self.assertEqual(result, "StUdLy - CaPs")

    def test_truncation(self):
        # Happy path: truncate without breaking words
        result = slugify_manual(" Call me maybe ", truncate=10)
        self.assertEqual(result, "call - me")

    def test_ignore_characters(self):
        # Happy path: preserve specific characters/words
        # Note: The spec example shows unicode characters being preserved
        result = slugify_manual("\u4f60 \u597d \uff0c \u4e16 \u754c", ignore=["\u4f60", "\u597d"])
        self.assertEqual(result, "\u4f60 \u597d - shi - jie")

    def test_empty_input(self):
        # Edge case: empty string
        self.assertIsNone(slugify_manual(""))

    def test_only_punctuation_input(self):
        # Edge case: input contains only invalid characters
        self.assertIsNone(slugify_manual("!!! @@@ ###"))

    def test_whitespace_handling(self):
        # Edge case: leading, trailing, and repeated whitespace
        result = slugify_manual("   foo    bar   ")
        self.assertEqual(result, "foo - bar")

    def test_small_truncate_value(self):
        # Edge case: truncate value so small that no words fit
        # If truncate is 1 and word is "hello", it might return None or empty depending on implementation
        # Based on spec: "may eliminate all words if none fit" -> returns None
        result = slugify_manual("hello", truncate=1)
        self.assertIsNone(result)

    def test_unicode_transliteration(self):
        # Happy path: mixed language input transliteration
        # "\u4f60 \u597d" is "ni hao"
        result = slugify_manual("\u4f60 \u597d")
        self.assertEqual(result, "ni - hao")

    def test_ignore_list_vs_string(self):
        # Test both string and list for ignore parameter
        result_str = slugify_manual("a!b", ignore="!")
        self.assertEqual(result_str, "a!b")
        
        result_list = slugify_manual("a!b", ignore=["!"])
        self.assertEqual(result_list, "a!b")

    def test_separator_as_integer(self):
        # Test separator as integer (UTF-8/binary) if applicable
        # Using a hyphen character's integer representation or similar
        # The spec says "separator= ( binary or UTF -8 integer )"
        # We test if it handles a valid integer input for a character
        result = slugify_manual("a b", separator=45) # 45 is '-'
        self.assertEqual(result, "a-b")

if __name__ == '__main__':
    unittest.main()