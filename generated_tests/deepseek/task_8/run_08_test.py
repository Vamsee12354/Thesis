import unittest
from implementation_manual import slugify_manual

class TestSlugifyManual(unittest.TestCase):
    def test_basic_slugify(self):
        self.assertEqual(slugify_manual("Hello, World!"), "hello-world")

    def test_empty_input(self):
        self.assertIsNone(slugify_manual(""))

    def test_punctuation_only(self):
        self.assertIsNone(slugify_manual("!@#$%^&*()"))

    def test_custom_separator(self):
        self.assertEqual(slugify_manual("Madam, I'm Adam", separator=""), "madamimadam")

    def test_lowercase_false(self):
        self.assertEqual(slugify_manual("StUdLy CaPs", lowercase=False), "StUdLy-CaPs")

    def test_truncate(self):
        self.assertEqual(slugify_manual("Call me maybe", truncate=10), "call-me")

    def test_ignore_characters(self):
        self.assertEqual(slugify_manual("你好, 世界", ignore=["你", "好"]), "你好-shi-jie")

    def test_leading_trailing_whitespace(self):
        self.assertEqual(slugify_manual("  foo bar  "), "foo-bar")

    def test_repeated_whitespace(self):
        self.assertEqual(slugify_manual("foo    bar"), "foo-bar")

    def test_mixed_language_input(self):
        self.assertEqual(slugify_manual("你好, 世界"), "ni-hao-shi-jie")

    def test_truncate_small_value(self):
        self.assertEqual(slugify_manual("Hello World", truncate=1), "h")

    def test_truncate_breaks_word(self):
        self.assertEqual(slugify_manual("Hello World", truncate=5), "hello")

    def test_ignore_list(self):
        self.assertEqual(slugify_manual("Hello, World!", ignore=["o"]), "helloo-world")

    def test_ignore_string(self):
        self.assertEqual(slugify_manual("Hello, World!", ignore="o"), "helloo-world")

    def test_invalid_truncate(self):
        with self.assertRaises(ValueError):
            slugify_manual("Hello, World!", truncate=-1)

    def test_invalid_separator(self):
        with self.assertRaises(ValueError):
            slugify_manual("Hello, World!", separator="invalid")

    def test_invalid_lowercase(self):
        with self.assertRaises(ValueError):
            slugify_manual("Hello, World!", lowercase="invalid")

    def test_invalid_ignore(self):
        with self.assertRaises(ValueError):
            slugify_manual("Hello, World!", ignore=123)

if __name__ == '__main__':
    unittest.main()