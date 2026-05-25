# Tests for task4_get_reading_duration
import unittest
from implementation_manual import get_read_duration

class Test_get_read_duration(unittest.TestCase):
    def test_no_text(self):
        self.assertEqual(get_read_duration(""),0)

        

if __name__ == "__main__":
    unittest.main()