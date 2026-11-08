import unittest
import math
from implementation_manual import get_read_duration

class TestGetReadDuration(unittest.TestCase):

    def test_empty_string_returns_one(self):
        # Setup
        text = ""
        
        # Action
        result = get_read_duration(text)
        
        # Verification
        self.assertEqual(result, 1)

    def test_whitespace_only_returns_one(self):
        # Setup
        text = "     "
        
        # Action
        result = get_read_duration(text)
        
        # Verification
        self.assertEqual(result, 1)

    def test_short_text_returns_one(self):
        # Setup
        text = "This is a short sentence."
        
        # Action
        result = get_read_duration(text)
        
        # Verification
        self.assertEqual(result, 1)

    def test_normal_paragraph_returns_one(self):
        # Setup
        # 50 words / 200 wpm = 0.25 minutes -> rounded up to 1
        text = "word " * 50
        
        # Action
        result = get_read_duration(text)
        
        # Verification
        self.assertEqual(result, 1)

    def test_long_post_returns_correct_minutes(self):
        # Setup
        # 450 words / 200 wpm = 2.25 minutes -> rounded up to 3
        text = "word " * 450
        
        # Action
        result = get_read_duration(text)
        
        # Verification
        self.assertEqual(result, 3)

    def test_exact_multiple_of_wpm(self):
        # Setup
        # 400 words / 200 wpm = 2.0 minutes
        text = "word " * 400
        
        # Action
        result = get_read_duration(text)
        
        # Verification
        self.assertEqual(result, 2)

    def test_non_latin_characters_whitespace_splitting(self):
        # Setup
        # Chinese text without spaces: "你好世界" is one token if no spaces
        text = "你好世界 你好世界" 
        
        # Action
        result = get_read_duration(text)
        
        # Verification
        # 2 tokens / 200 wpm = 0.01 -> rounded up to 1
        self.assertEqual(result, 1)

    def test_large_whitespace_separation(self):
        # Setup
        # Testing that multiple spaces between words don't inflate word count
        text = "word    word\nword\tword"
        
        # Action
        result = get_read_duration(text)
        
        # Verification
        # 4 words / 200 wpm = 0.02 -> rounded up to 1
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()