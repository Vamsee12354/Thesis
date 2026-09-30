import unittest
from implementation_manual import slugify_manual

class TestSlugifyManual(unittest.TestCase):

    def test_basic_slugification(self):
        # Happy path: standard string with punctuation and spaces
        result = slugify_manual(" Hello , World !")
        self.assertEqual(result, "hello - world")

    def test_custom_separator(self):
        # Happy path: custom separator (empty string)
        result = slugify_manual(" Madam , I'm Adam ", separator="")
        self.assertEqual(result, "madamimadam")

    def test_case_preservation(self):
        # Happy path: disable lowercase
        result = slugify_manual(" StUdLy CaPs ", lowercase=False)
        self.assertEqual(result, "StUdLy - CaPs")

    def test_truncation(self):
        # Happy path: truncate without breaking words
        result = slugify_manual(" Call me maybe ", truncate=10)
        self.assertEqual(result, "call - me")

    def test_ignore_characters(self):
        # Happy path: preserve specific characters/strings
        # Note: The spec example shows unicode characters being ignored
        result = slugify_manual("\u4f60 \u597d \uff0c \u4e16 \u754c", ignore=["\u4f60", "\u597d"])
        self.assertEqual(result, "\u4f60\u597d - shi - jie")

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
        # Edge case: very small truncate value that might eliminate words
        # If truncate is 1 and word is "a", it might work, but if it's too small for any word:
        result = slugify_manual("Hello World", truncate=1)
        # Based on spec "may eliminate all words if none fit", we check if it returns None or empty
        # Given the spec says "Returns None if no valid slug can be generated"
        self.assertIsNone(result)

    def test_unicode_transliteration(self):
        # Happy path: mixed language input transliteration
        # "\u4f60 \u597d" is "你好" (Ni Hao)
        result = slugify_manual("\u4f60 \u597d")
        self.assertEqual(result, "ni - hao")

    def test_ignore_list_vs_string(self):
        # Test both string and list for the ignore parameter
        result_str = slugify_manual("a!b", ignore="!")
        self.assertEqual(result_str, "a!b")
        
        result_list = slugify_manual("a!b", ignore=["!"])
        self.assertEqual(result_list, "a!b")

if __name__ == '__main__':
    unittest.main()