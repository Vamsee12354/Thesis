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

    def test_punctuation_only_input_returns_none(self):
        # Arrange
        text = "!!!,,,;;;..."
        # Act
        result = slugify_manual(text)
        # Assert
        self.assertIsNone(result)

    def test_separator_empty_string(self):
        # Arrange
        text = "Madam , I ’m Adam "
        expected = "madamimadam"
        # Act
        result = slugify_manual(text, separator="")
        # Assert
        self.assertEqual(result, expected)

    def test_lowercase_false_preserves_case(self):
        # Arrange
        text = "StUdLy CaPs "
        expected = "StUdLy-CaPs"
        # Act
        result = slugify_manual(text, lowercase=False)
        # Assert
        self.assertEqual(result, expected)

    def test_truncate_shortens_without_breaking_words(self):
        # Arrange
        text = "Call me maybe "
        expected = "call-me"
        # Act
        result = slugify_manual(text, truncate=10)
        # Assert
        self.assertEqual(result, expected)

    def test_truncate_too_small_returns_none(self):
        # Arrange
        text = "Call me maybe"
        # Act
        result = slugify_manual(text, truncate=1)
        # Assert
        self.assertIsNone(result)

    def test_ignore_characters_preserved(self):
        # Arrange
        text = "你好，世界 "
        expected = "你好-shi-jie"
        # Act
        result = slugify_manual(text, ignore=["你", "好"])
        # Assert
        self.assertEqual(result, expected)

    def test_ignore_as_string_preserves_characters(self):
        # Arrange
        text = "你好，世界 "
        expected = "你好-shi-jie"
        # Act
        result = slugify_manual(text, ignore="你好")
        # Assert
        self.assertEqual(result, expected)

    def test_custom_separator_utf8_integer(self):
        # Arrange
        text = "Hello World"
        expected = "hello_world"
        # Act
        result = slugify_manual(text, separator=95)  # ASCII for underscore
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

    def test_ignore_with_punctuation(self):
        # Arrange
        text = "Hello, world!"
        expected = "hello,-world"
        # Act
        result = slugify_manual(text, ignore=[","])
        # Assert
        self.assertEqual(result, expected)

    def test_no_valid_slug_due_to_ignore_and_truncate(self):
        # Arrange
        text = "Hello world"
        # Act
        result = slugify_manual(text, ignore=["h","e","l","o","w","r","d"], truncate=2)
        # Assert
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()