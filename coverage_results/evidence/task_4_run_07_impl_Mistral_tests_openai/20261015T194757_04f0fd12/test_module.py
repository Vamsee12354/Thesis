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

    def test_single_word_returns_one_minute(self):
        # Arrange
        text = "Hello"
        # Act
        result = get_read_duration(text)
        # Assert
        self.assertEqual(result, 1)

    def test_exact_200_words_returns_one_minute(self):
        # Arrange
        text = "word " * 200
        # Act
        result = get_read_duration(text)
        # Assert
        self.assertEqual(result, 1)

    def test_201_words_returns_two_minutes(self):
        # Arrange
        text = "word " * 201
        # Act
        result = get_read_duration(text)
        # Assert
        self.assertEqual(result, 2)

    def test_450_words_returns_three_minutes(self):
        # Arrange
        text = "word " * 450
        # Act
        result = get_read_duration(text)
        # Assert
        self.assertEqual(result, 3)

    def test_text_with_multiple_spaces_between_words(self):
        # Arrange
        text = "word    word  word"
        # Act
        result = get_read_duration(text)
        # Assert
        self.assertEqual(result, 1)

    def test_text_with_newlines_and_tabs(self):
        # Arrange
        text = "word\nword\tword"
        # Act
        result = get_read_duration(text)
        # Assert
        self.assertEqual(result, 1)

    def test_non_latin_characters_counted_as_words(self):
        # Arrange
        text = "这是 一个 测试"  # 4 tokens separated by spaces
        # Act
        result = get_read_duration(text)
        # Assert
        self.assertEqual(result, 1)

    def test_long_non_latin_text_with_spaces(self):
        # Arrange
        text = "词 " * 400  # 400 tokens
        # Act
        result = get_read_duration(text)
        # Assert
        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()