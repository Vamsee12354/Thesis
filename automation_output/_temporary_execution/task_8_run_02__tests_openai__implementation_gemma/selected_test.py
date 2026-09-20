import unittest
from implementation_manual import slugify_manual

class TestSlugifyManual(unittest.TestCase):

    def test_basic_slugification(self):
        # Arrange
        text = " Hello , World !"
        expected = "hello-world"
        # Act
        result = slugify_manual(text)
        # Assert
        self.assertEqual(result, expected)

    def test_empty_input_returns_none(self):
        # Arrange
        text = ""
        # Act
        result = slugify_manual(text)
        # Assert
        self.assertIsNone(result)

    def test_punctuation_only_returns_none(self):
        # Arrange
        text = "!@#$%^&*()"
        # Act
        result = slugify_manual(text)
        # Assert
        self.assertIsNone(result)

    def test_separator_empty_string(self):
        # Arrange
        text = " Madam , I ’m Adam "
        expected = "madamimadam"
        # Act
        result = slugify_manual(text, separator="")
        # Assert
        self.assertEqual(result, expected)

    def test_case_preservation(self):
        # Arrange
        text = " StUdLy CaPs "
        expected = "StUdLy-CaPs"
        # Act
        result = slugify_manual(text, lowercase=False)
        # Assert
        self.assertEqual(result, expected)

    def test_truncate_long_text(self):
        # Arrange
        text = " Call me maybe "
        expected = "call-me"
        # Act
        result = slugify_manual(text, truncate=10)
        # Assert
        self.assertEqual(result, expected)

    def test_truncate_small_value_eliminates_words(self):
        # Arrange
        text = " Call me maybe "
        # Act
        result = slugify_manual(text, truncate=1)
        # Assert
        self.assertIsNone(result)

    def test_ignore_characters_preserved(self):
        # Arrange
        text = "\u4f60\u597d\uff0c\u4e16\u754c"
        ignore = ["\u4f60", "\u597d"]
        expected = "\u4f60\u597d-shi-jie"
        # Act
        result = slugify_manual(text, ignore=ignore)
        # Assert
        self.assertEqual(result, expected)

    def test_ignore_as_string(self):
        # Arrange
        text = "foo@bar.com"
        ignore = "@"
        expected = "foo@bar-com"
        # Act
        result = slugify_manual(text, ignore=ignore)
        # Assert
        self.assertEqual(result, expected)

    def test_leading_trailing_and_repeated_whitespace(self):
        # Arrange
        text = "  foo   bar  "
        expected = "foo-bar"
        # Act
        result = slugify_manual(text)
        # Assert
        self.assertEqual(result, expected)

    def test_non_ascii_transliteration(self):
        # Arrange
        text = "café"
        expected = "cafe"
        # Act
        result = slugify_manual(text)
        # Assert
        self.assertEqual(result, expected)

    def test_separator_utf8_integer(self):
        # Arrange
        text = "foo bar"
        separator = ord("_")
        expected = "foo_bar"
        # Act
        result = slugify_manual(text, separator=separator)
        # Assert
        self.assertEqual(result, expected)

    def test_all_invalid_characters_after_ignore(self):
        # Arrange
        text = "!@#$"
        ignore = ["!"]
        # Act
        result = slugify_manual(text, ignore=ignore)
        # Assert
        self.assertIsNone(result)

    def test_slugify_with_multiple_ignore_characters(self):
        # Arrange
        text = "foo@bar#baz"
        ignore = ["@", "#"]
        expected = "foo@bar#baz"
        # Act
        result = slugify_manual(text, ignore=ignore, separator="")
        # Assert
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()