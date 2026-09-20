import unittest
from implementation_manual import get_read_duration

class TestGetReadDuration(unittest.TestCase):

    def test_empty_string_returns_minimum_one(self):
        # Arrange
        text = ""
        # Act
        result = get_read_duration(text)
        # Assert
        self.assertEqual(result, 1)

    def test_string_with_only_whitespace_returns_minimum_one(self):
        # Arrange
        text = "     \t  \n  "
        # Act
        result = get_read_duration(text)
        # Assert
        self.assertEqual(result, 1)

    def test_short_text_less_than_200_words_returns_one(self):
        # Arrange
        text = "This is a simple blog post with about fifty words total " * 1
        # Act
        result = get_read_duration(text)
        # Assert
        self.assertEqual(result, 1)

    def test_exactly_200_words_returns_one(self):
        # Arrange
        text = "word " * 200
        # Act
        result = get_read_duration(text)
        # Assert
        self.assertEqual(result, 1)

    def test_just_over_200_words_returns_two(self):
        # Arrange
        text = "word " * 201
        # Act
        result = get_read_duration(text)
        # Assert
        self.assertEqual(result, 2)

    def test_long_text_multiple_minutes(self):
        # Arrange
        text = "word " * 450
        # Act
        result = get_read_duration(text)
        # Assert
        self.assertEqual(result, 3)

    def test_text_with_excessive_whitespace_between_words(self):
        # Arrange
        text = "word    word\tword\nword  word"
        # Act
        result = get_read_duration(text)
        # Assert
        self.assertEqual(result, 1)

    def test_text_with_non_latin_characters(self):
        # Arrange
        text = "这是 一个 测试 文本 with some English words"
        # Act
        result = get_read_duration(text)
        # Assert
        # The count depends on whitespace splitting, so expect at least 1
        self.assertTrue(result >= 1)

    def test_text_with_newlines_and_tabs(self):
        # Arrange
        text = "word\nword\tword word\n\nword"
        # Act
        result = get_read_duration(text)
        # Assert
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()