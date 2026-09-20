import unittest
import math
from implementation_manual import get_read_duration

class TestGetReadDuration(unittest.TestCase):

    def test_empty_string_returns_one(self):
        # Arrange
        text = ""
        
        # Act
        result = get_read_duration(text)
        
        # Assert
        self.assertEqual(result, 1)

    def test_whitespace_only_returns_one(self):
        # Arrange
        text = "     "
        
        # Act
        result = get_read_duration(text)
        
        # Assert
        self.assertEqual(result, 1)

    def test_short_text_returns_one(self):
        # Arrange
        text = "This is a short sentence."
        
        # Act
        result = get_read_duration(text)
        
        # Assert
        self.assertEqual(result, 1)

    def test_normal_paragraph_returns_one(self):
        # Arrange
        # 50 words / 200 wpm = 0.25 minutes -> rounded up to 1
        text = "word " * 50
        
        # Act
        result = get_read_duration(text)
        
        # Assert
        self.assertEqual(result, 1)

    def test_long_post_returns_correct_minutes(self):
        # Arrange
        # 450 words / 200 wpm = 2.25 minutes -> rounded up to 3
        text = "word " * 450
        
        # Act
        result = get_read_duration(text)
        
        # Assert
        self.assertEqual(result, 3)

    def test_exact_word_count_boundary(self):
        # Arrange
        # 200 words / 200 wpm = 1 minute
        text = "word " * 200
        
        # Act
        result = get_read_duration(text)
        
        # Assert
        self.assertEqual(result, 1)

    def test_just_over_boundary_rounds_up(self):
        # Arrange
        # 201 words / 200 wpm = 1.005 minutes -> rounded up to 2
        text = "word " * 201
        
        # Act
        result = get_read_duration(text)
        
        # Assert
        self.assertEqual(result, 2)

    def test_non_latin_characters_whitespace_splitting(self):
        # Arrange
        # Chinese text without spaces: "你好世界" is one token by whitespace splitting
        text = "你好世界 你好世界"
        
        # Act
        result = get_read_duration(text)
        
        # Assert
        # 2 tokens / 200 wpm = 0.01 -> rounded up to 1
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()