from implementation_manual import slugify_manual
import unittest

class TestSlugifyManual(unittest.TestCase):
    def test_basic_conversion(self):
        self.assertEqual(slugify_manual("Hello World"), "hello-world")
    
    def test_empty_string(self):
        self.assertIsNone(slugify_manual(""))
    
    def test_punctuation_only(self):
        self.assertIsNone(slugify_manual("!@#$%^&*()"))
    
    def test_mixed_case(self):
        self.assertEqual(slugify_manual("StUdLy CaPs", lowercase=False), "StUdLy-CaPs")
    
    def test_custom_separator(self):
        self.assertEqual(slugify_manual("foo bar", separator="_"), "foo_bar")
    
    def test_truncation(self):
        self.assertEqual(slugify_manual("This is a long string", truncate=10), "this-is-a")
    
    def test_unicode_transliteration(self):
        self.assertEqual(slugify_manual("你好，世界"), "ni-hao-shi-jie")
    
    def test_ignored_characters(self):
        self.assertEqual(slugify_manual("你好，世界", ignore=["你","好"]), "你好-shi-jie")
    
    def test_multiple_spaces(self):
        self.assertEqual(slugify_manual("foo    bar"), "foo-bar")
    
    def test_leading_trailing_spaces(self):
        self.assertEqual(slugify_manual("  foo bar  "), "foo-bar")
    
    def test_no_spaces(self):
        self.assertEqual(slugify_manual("foobar"), "foobar")
    
    def test_empty_after_processing(self):
        self.assertIsNone(slugify_manual("  "))
    
    def test_separator_only(self):
        self.assertEqual(slugify_manual("foo-bar", separator="+"), "foo+bar")
    
    def test_truncate_too_small(self):
        self.assertIsNone(slugify_manual("foo bar", truncate=1))
    
    def test_preserve_ignored_chars(self):
        self.assertEqual(slugify_manual("foo@bar", ignore=["@"]), "foo@bar")
    
    def test_mixed_chars_with_ignore(self):
        self.assertEqual(slugify_manual("foo!bar", ignore=["!"]), "foo!bar")
    
    def test_numeric_input(self):
        self.assertEqual(slugify_manual("123 456"), "123-456")
    
    def test_mixed_alphanumeric(self):
        self.assertEqual(slugify_manual("abc123 def456"), "abc123-def456")
    
    def test_custom_separator_multichar(self):
        self.assertEqual(slugify_manual("foo bar", separator="++"), "foo++bar")