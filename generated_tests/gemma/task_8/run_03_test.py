import unittest
from implementation_manual import slugify_manual

class TestSlugifyManual(unittest.TestCase):

    def test_basic_slugification(self):
        # Happy path: standard string with punctuation and whitespace
        # Expected: "hello-world" (assuming default separator is ' - ')
        # Note: The spec example shows " hello - world " with spaces around the dash.
        # We follow the example's behavior.
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
        # "call - me" is 9 chars. "call - me maybe" truncated at 10.
        result = slugify_manual(" Call me maybe ", truncate=10)
        self.assertEqual(result, "call - me")

    def test_ignore_characters(self):
        # Happy path: preserve specific characters/words via ignore
        # Input: "\u4f60 \u597d \uff0c \u4e16 \u754c" (你好，世界)
        # If \u4f60 and \u597d are ignored, they stay.
        # The spec example shows: "\u4f60 \u597d - shi - jie"
        result = slugify_manual("\u4f60 \u597d \uff0c \u4e16 \u754c", ignore=["\u4f60", "\u597d"])
        self.assertEqual(result, "\u4f60 \u597d - shi - jie")

    def test_empty_input(self):
        # Edge case: empty string
        self.assertIsNone(slugify_manual(""))

    def test_only_punctuation_input(self):
        # Edge case: input contains only invalid characters/punctuation
        self.assertIsNone(slugify_manual("!!! @@@ ###"))

    def test_whitespace_handling(self):
        # Edge case: leading, trailing, and repeated whitespace
        result = slugify_manual("   foo    bar   ")
        self.assertEqual(result, "foo - bar")

    def test_small_truncate_value(self):
        # Edge case: truncate value so small that no words fit
        # "hello" is 5 chars. Truncate 2.
        result = slugify_manual("hello", truncate=2)
        self.assertIsNone(result)

    def test_unicode_transliteration(self):
        # Happy path: transliteration of non-ASCII
        # "你好" -> "ni - hao"
        result = slugify_manual("\u4f60\u597d")
        self.assertEqual(result, "ni - hao")

    def test_ignore_list_vs_string(self):
        # Verify ignore works with both string and list
        # Test with string
        res_str = slugify_manual("a!b", ignore="!")
        self.assertEqual(res_str, "a!b")
        # Test with list
        res_list = slugify_manual("a!b", ignore=["!"])
        self.assertEqual(res_list, "a!b")

if __name__ == '__main__':
    unittest.main()