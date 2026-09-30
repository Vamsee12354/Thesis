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
        text = "Madam , I ’m Adam"
        expected = "madamimadam"
        # Act
        result = slugify_manual(text, separator="")
        # Assert
        self.assertEqual(result, expected)

    def test_lowercase_false_preserves_case(self):
        # Arrange
        text = "StUdLy CaPs"
        expected = "StUdLy-CaPs"
        # Act
        result = slugify_manual(text, lowercase=False)
        # Assert
        self.assertEqual(result, expected)

    def test_truncate_does_not_break_words(self):
        # Arrange
        text = "Call me maybe"
        expected = "call-me"
        # Act
        result = slugify_manual(text, truncate=10)
        # Assert
        self.assertEqual(result, expected)

    def test_truncate_too_small_eliminates_all_words(self):
        # Arrange
        text = "Call me maybe"
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

    def test_ignore_as_string_preserves_characters(self):
        # Arrange
        text = "Hello, world!"
        ignore = ","
        expected = "hello,-world"
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
        text = "Café"
        expected = "cafe"
        # Act
        result = slugify_manual(text)
        # Assert
        self.assertEqual(result, expected)

    def test_custom_separator_utf8_integer(self):
        # Arrange
        text = "Hello World"
        separator = ord("_")
        expected = "hello_world"
        # Act
        result = slugify_manual(text, separator=separator)
        # Assert
        self.assertEqual(result, expected)

    def test_ignore_list_and_lowercase_false(self):
        # Arrange
        text = "Hello, World!"
        ignore = [","]
        expected = "Hello,-World"
        # Act
        result = slugify_manual(text, ignore=ignore, lowercase=False)
        # Assert
        self.assertEqual(result, expected)

    def test_input_with_only_ignored_characters(self):
        # Arrange
        text = "!!!"
        ignore = ["!"]
        expected = "!!!"
        # Act
        result = slugify_manual(text, ignore=ignore)
        # Assert
        self.assertEqual(result, expected)

    def test_truncate_exact_word_length(self):
        # Arrange
        text = "hello world"
        expected = "hello"
        # Act
        result = slugify_manual(text, truncate=5)
        # Assert
        self.assertEqual(result, expected)

    def test_truncate_with_separator_length(self):
        # Arrange
        text = "hello world"
        expected = "hello-world"
        # Act
        result = slugify_manual(text, truncate=11)
        # Assert
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()