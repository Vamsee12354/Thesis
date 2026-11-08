import unittest
from implementation_manual import slugify_manual

class TestSlugifyManual(unittest.TestCase):

    def test_basic_slugification_default(self):
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

    def test_slugify_with_no_lowercase(self):
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

    def test_slugify_with_ignore_list(self):
        # Arrange
        text = "你好，世界 "
        expected = "你好-shi-jie"
        ignore = ["你", "好"]
        # Act
        result = slugify_manual(text, ignore=ignore)
        # Assert
        self.assertEqual(result, expected)

    def test_slugify_empty_string(self):
        # Arrange
        text = ""
        # Act
        result = slugify_manual(text)
        # Assert
        self.assertIsNone(result)

    def test_slugify_only_punctuation(self):
        # Arrange
        text = "!@#$%^&*()"
        # Act
        result = slugify_manual(text)
        # Assert
        self.assertIsNone(result)

    def test_slugify_truncate_too_small(self):
        # Arrange
        text = "Hello world"
        # Act
        result1 = slugify_manual(text, truncate=1)
        result2 = slugify_manual(text, truncate=2)
        # Assert
        self.assertIsNone(result1)
        self.assertIsNone(result2)

    def test_slugify_leading_trailing_whitespace(self):
        # Arrange
        text = "   foo   bar   "
        expected = "foo-bar"
        # Act
        result = slugify_manual(text)
        # Assert
        self.assertEqual(result, expected)

    def test_slugify_repeated_whitespace(self):
        # Arrange
        text = "foo    bar"
        expected = "foo-bar"
        # Act
        result = slugify_manual(text)
        # Assert
        self.assertEqual(result, expected)

    def test_slugify_custom_separator_utf8(self):
        # Arrange
        text = "foo bar"
        expected = "foo_bar"
        # Act
        result = slugify_manual(text, separator="_")
        # Assert
        self.assertEqual(result, expected)

    def test_slugify_ignore_string(self):
        # Arrange
        text = "你好，世界 "
        expected = "你好-shi-jie"
        ignore = "你好"
        # Act
        result = slugify_manual(text, ignore=ignore)
        # Assert
        self.assertEqual(result, expected)

    def test_slugify_ignore_preserves_characters(self):
        # Arrange
        text = "foo@bar.com"
        expected = "foo@bar-com"
        ignore = ["@"]
        # Act
        result = slugify_manual(text, ignore=ignore)
        # Assert
        self.assertEqual(result, expected)

    def test_slugify_non_ascii_transliteration(self):
        # Arrange
        text = "Café"
        expected = "cafe"
        # Act
        result = slugify_manual(text)
        # Assert
        self.assertEqual(result, expected)

    def test_slugify_ignore_with_multiple_characters(self):
        # Arrange
        text = "foo@bar#baz"
        expected = "foo@bar#baz"
        ignore = ["@", "#"]
        # Act
        result = slugify_manual(text, separator="", ignore=ignore, lowercase=False)
        # Assert
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()