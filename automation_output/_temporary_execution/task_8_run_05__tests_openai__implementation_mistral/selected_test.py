import unittest
from implementation_manual import slugify_manual

class TestSlugifyManual(unittest.TestCase):

    def test_basic_slugification_lowercase_default_separator(self):
        # Arrange
        text = " Hello , World !"
        expected = "hello-world"
        # Act
        result = slugify_manual(text)
        # Assert
        self.assertEqual(result, expected)

    def test_slugify_with_empty_separator(self):
        # Arrange
        text = "Madam , I ’m Adam "
        expected = "madamimadam"
        # Act
        result = slugify_manual(text, separator="")
        # Assert
        self.assertEqual(result, expected)

    def test_slugify_preserve_case(self):
        # Arrange
        text = "StUdLy CaPs "
        expected = "StUdLy-CaPs"
        # Act
        result = slugify_manual(text, lowercase=False)
        # Assert
        self.assertEqual(result, expected)

    def test_slugify_with_truncate(self):
        # Arrange
        text = "Call me maybe "
        expected = "call-me"
        # Act
        result = slugify_manual(text, truncate=10)
        # Assert
        self.assertEqual(result, expected)

    def test_slugify_with_ignore_characters(self):
        # Arrange
        text = "你好，世界 "
        expected = "你好-shi-jie"
        ignore = ["你", "好"]
        # Act
        result = slugify_manual(text, ignore=ignore)
        # Assert
        self.assertEqual(result, expected)

    def test_empty_input_returns_none(self):
        # Arrange
        text = ""
        # Act
        result = slugify_manual(text)
        # Assert
        self.assertIsNone(result)

    def test_punctuation_only_input_returns_none(self):
        # Arrange
        text = "!@#$%^&*()"
        # Act
        result = slugify_manual(text)
        # Assert
        self.assertIsNone(result)

    def test_truncate_too_small_to_fit_any_word_returns_none(self):
        # Arrange
        text = "hello world"
        # Act
        result = slugify_manual(text, truncate=1)
        # Assert
        self.assertIsNone(result)

    def test_truncate_exact_word_fit(self):
        # Arrange
        text = "hello world"
        expected = "hello"
        # Act
        result = slugify_manual(text, truncate=5)
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

    def test_mixed_language_transliteration(self):
        # Arrange
        text = "你好世界"
        expected = "ni-hao-shi-jie"
        # Act
        result = slugify_manual(text)
        # Assert
        self.assertEqual(result, expected)

    def test_ignore_preserves_characters(self):
        # Arrange
        text = "a!b@c#d$"
        ignore = ["!", "@", "#"]
        expected = "a!b@c-d"
        # Act
        result = slugify_manual(text, ignore=ignore)
        # Assert
        self.assertEqual(result, expected)

    def test_separator_as_utf8_integer(self):
        # Arrange
        text = "foo bar"
        separator = ord("_")
        expected = "foo_bar"
        # Act
        result = slugify_manual(text, separator=separator)
        # Assert
        self.assertEqual(result, expected)

    def test_lowercase_false_with_ignore(self):
        # Arrange
        text = "Hello 世界"
        ignore = ["世"]
        expected = "Hello-世-jie"
        # Act
        result = slugify_manual(text, lowercase=False, ignore=ignore)
        # Assert
        self.assertEqual(result, expected)

    def test_ignore_as_string(self):
        # Arrange
        text = "a!b@c#d$"
        ignore = "!"
        expected = "a!b-c-d"
        # Act
        result = slugify_manual(text, ignore=ignore)
        # Assert
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()