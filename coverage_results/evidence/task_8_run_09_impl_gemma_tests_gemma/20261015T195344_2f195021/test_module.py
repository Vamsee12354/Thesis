import unittest
from implementation_manual import slugify_manual

class TestSlugifyManual(unittest.TestCase):

    def test_basic_slugification(self):
        # Happy path: standard string
        self.assertEqual(slugify_manual("Hello World"), "hello-world")
        # Happy path: mixed case and punctuation
        self.assertEqual(slugify_manual("Hello, World!"), "hello-world")

    def test_separator_customization(self):
        # Custom separator (empty string)
        self.assertEqual(slugify_manual("Madam, I'm Adam", separator=""), "madamimadam")
        # Custom separator (underscore)
        self.assertEqual(slugify_manual("Hello World", separator="_"), "hello_world")

    def test_lowercase_option(self):
        # Disable lowercase
        self.assertEqual(slugify_manual("StUdLy CaPs", lowercase=False), "StUdLy-CaPs")
        # Default lowercase
        self.assertEqual(slugify_manual("UPPER"), "upper")

    def test_ignore_parameter(self):
        # Ignore specific characters (list)
        self.assertEqual(slugify_manual("你好，世界", ignore=["你", "好"]), "你好-shi-jie")
        # Ignore specific characters (string)
        self.assertEqual(slugify_manual("a!b@c", ignore="!@"), "abc")

    def test_truncation(self):
        # Truncate without breaking words
        self.assertEqual(slugify_manual("Call me maybe", truncate=10), "call-me")
        # Truncate very small
        self.assertEqual(slugify_manual("abc def", truncate=3), "abc")
        # Truncate where no words fit
        self.assertEqual(slugify_manual("a b c", truncate=1), None)

    def test_whitespace_handling(self):
        # Leading, trailing, and repeated whitespace
        self.assertEqual(slugify_manual("   foo    bar   "), "foo-bar")
        self.assertEqual(slugify_manual("\tfoo\nbar\r"), "foo-bar")

    def test_unicode_transliteration(self):
        # Transliteration of non-ASCII
        # Note: Exact transliteration depends on implementation, 
        # but based on spec "你好" => "ni-hao"
        self.assertEqual(slugify_manual("你好"), "ni-hao")

    def test_invalid_inputs_and_edge_cases(self):
        # Empty input
        self.assertIsNone(slugify_manual(""))
        # Only punctuation/invalid characters
        self.assertIsNone(slugify_manual("!!! ???"))
        # Input that becomes empty after cleaning
        self.assertIsNone(slugify_manual("   "))

    def test_complex_combinations(self):
        # Combination of separator, lowercase, and ignore
        # "A! B? C" with separator "_" and ignore "!" -> "a!_b_c" (if lowercase is True)
        # However, spec says "A! B? C" with ignore "!" and separator "_" and lowercase False
        self.assertEqual(slugify_manual("A! B? C", separator="_", lowercase=False, ignore="!"), "A!-B-C")

if __name__ == '__main__':
    unittest.main()