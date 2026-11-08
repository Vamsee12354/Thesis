import unittest
from implementation_manual import slugify_manual

class TestSlugifyManual(unittest.TestCase):
    def test_basic_conversion(self):
        self.assertEqual(slugify_manual("Hello World"), "hello-world")
    
    def test_empty_input(self):
        self.assertIsNone(slugify_manual(""))
    
    def test_punctuation_only(self):
        self.assertIsNone(slugify_manual("!@#$%^&*()"))
    
    def test_custom_separator(self):
        self.assertEqual(slugify_manual("foo bar", separator="_"), "foo_bar")
    
    def test_preserve_case(self):
        self.assertEqual(slugify_manual("StUdLy CaPs", lowercase=False), "StUdLy-CaPs")
    
    def test_truncation(self):
        self.assertEqual(slugify_manual("Call me maybe", truncate=10), "call-me")
    
    def test_ignored_characters(self):
        self.assertEqual(slugify_manual("你好，世界", ignore=["你","好"]), "你好-shi-jie")
    
    def test_leading_trailing_whitespace(self):
        self.assertEqual(slugify_manual("  foo bar  "), "foo-bar")
    
    def test_repeated_whitespace(self):
        self.assertEqual(slugify_manual("foo    bar"), "foo-bar")
    
    def test_mixed_language(self):
        self.assertEqual(slugify_manual("Привет мир"), "privet-mir")
    
    def test_all_ignored(self):
        self.assertEqual(slugify_manual("!@#$%", ignore="!@#$%"), "!@#$%")
    
    def test_truncate_too_small(self):
        self.assertIsNone(slugify_manual("foo bar", truncate=1))
    
    def test_no_valid_characters(self):
        self.assertIsNone(slugify_manual("-- --"))
    
    def test_unicode_characters(self):
        self.assertEqual(slugify_manual("café"), "cafe")
    
    def test_numbers_preserved(self):
        self.assertEqual(slugify_manual("version 2.0"), "version-20")
    
    def test_custom_ignore_list(self):
        self.assertEqual(slugify_manual("a!b@c#", ignore=["@"]), "ab@c")