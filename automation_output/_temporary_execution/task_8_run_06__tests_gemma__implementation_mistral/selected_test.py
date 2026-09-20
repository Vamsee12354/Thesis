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
        # Happy path: disabling lowercase
        result = slugify_manual(" StUdLy CaPs ", lowercase=False)
        self.assertEqual(result, "StUdLy - CaPs")

    def test_truncation(self):
        # Happy path: truncation without breaking words
        result = slugify_manual(" Call me maybe ", truncate=10)
        self.assertEqual(result, "call - me")

    def test_ignore_characters(self):
        # Happy path: preserving specific characters via ignore list
        # Note: The spec example shows unicode characters being preserved
        result = slugify_manual("\u4f60 \u597d \uff0c \u4e16 \u754c", ignore=["\u4f60", "\u597d"])
        self.assertEqual(result, "\u4f60 \u597d - shi - jie")

    def test_unicode_transliteration(self):
        # Happy path: transliterating unicode to alphanumeric
        # Based on spec example: "\u4f60 \u597d" => "ni - hao"
        result = slugify_manual("\u4f60 \u597d")
        self.assertEqual(result, "ni - hao")

    def test_empty_input(self):
        # Edge case: empty string returns None
        self.assertIsNone(slugify_manual(""))

    def test_only_punctuation_input(self):
        # Edge case: input with only punctuation returns None
        self.assertIsNone(slugify_manual("!!! ??? ,,, "))

    def test_whitespace_handling(self):
        # Edge case: leading, trailing, and repeated whitespace
        result = slugify_manual("   foo    bar   ")
        self.assertEqual(result, "foo - bar")

    def test_small_truncate_value(self):
        # Edge case: very small truncate value that eliminates words
        # If truncate is 1, and words are longer, it might return None or empty
        # Based on spec: "may eliminate all words if none fit"
        result = slugify_manual("Hello World", truncate=1)
        self.assertIsNone(result)

    def test_ignore_single_string(self):
        # Happy path: ignore parameter as a single string
        result = slugify_manual("Hello! World", ignore="!")
        self.assertEqual(result, "hello! - world")

    def test_alphanumeric_only(self):
        # Happy path: input already clean
        result = slugify_manual("simple123")
        self.assertEqual(result, "simple123")

if __name__ == '__main__':
    unittest.main()