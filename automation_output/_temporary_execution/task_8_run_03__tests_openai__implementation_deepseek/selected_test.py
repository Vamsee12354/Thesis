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

    def test_slugify_with_empty_separator(self):
        # Arrange
        text = " Madam , I ’m Adam "
        expected = "madamimadam"
        # Act
        result = slugify_manual(text, separator="")
        # Assert
        self.assertEqual(result, expected)

    def test_slugify_with_no_lowercase(self):
        # Arrange
        text = " StUdLy CaPs "
        expected = "StUdLy-CaPs"
        # Act
        result = slugify_manual(text, lowercase=False)
        # Assert
        self.assertEqual(result, expected)

    def test_slugify_with_truncate(self):
        # Arrange
        text = " Call me maybe "
        expected = "call-me"
        # Act
        result = slugify_manual(text, truncate=10)
        # Assert
        self.assertEqual(result, expected)

    def test_slugify_with_ignore_unicode(self):
        # Arrange
        text = "\u4f60\u597d\uff0c\u4e16\u754c"
        ignore = ["\u4f60", "\u597d"]
        expected = "\u4f60\u597d-shi-jie"
        # Act
        result = slugify_manual(text, ignore=ignore)
        # Assert
        self.assertEqual(result, expected)

    def test_slugify_empty_input(self):
        # Arrange
        text = ""
        # Act
        result = slugify_manual(text)
        # Assert
        self.assertIsNone(result)

    def test_slugify_punctuation_only_input(self):
        # Arrange
        text = "!@#$%^&*()"
        # Act
        result = slugify_manual(text)
        # Assert
        self.assertIsNone(result)

    def test_slugify_truncate_too_small(self):
        # Arrange
        text = "hello world"
        # Act
        result_1 = slugify_manual(text, truncate=1)
        result_2 = slugify_manual(text, truncate=2)
        # Assert
        self.assertIsNone(result_1)
        self.assertIsNone(result_2)

    def test_slugify_leading_trailing_repeated_whitespace(self):
        # Arrange
        text = "   foo   bar   "
        expected = "foo-bar"
        # Act
        result = slugify_manual(text)
        # Assert
        self.assertEqual(result, expected)

    def test_slugify_mixed_language_transliteration(self):
        # Arrange
        text = "\u4f60\u597d"
        expected = "ni-hao"
        # Act
        result = slugify_manual(text)
        # Assert
        self.assertEqual(result, expected)

    def test_slugify_ignore_preserves_characters(self):
        # Arrange
        text = "a!b@c#d$"
        ignore = ["!", "@", "#"]
        expected = "a!b@c-d"
        # Act
        result = slugify_manual(text, ignore=ignore)
        # Assert
        self.assertEqual(result, expected)

    def test_slugify_custom_separator_utf8(self):
        # Arrange
        text = "hello world"
        separator = "★"
        expected = "hello★world"
        # Act
        result = slugify_manual(text, separator=separator)
        # Assert
        self.assertEqual(result, expected)

    def test_slugify_ignore_as_string(self):
        # Arrange
        text = "a!b@c#d$"
        ignore = "!@#"
        expected = "a!b@c-d"
        # Act
        result = slugify_manual(text, ignore=ignore)
        # Assert
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()