import unittest
from implementation_manual import slugify_manual

class TestSlugifyManual(unittest.TestCase):
    def test_basic_slug(self):
        result = slugify_manual("Hello, World!")
        self.assertEqual(result, "hello-world")

    def test_empty_input(self):
        result = slugify_manual("")
        self.assertIsNone(result)

    def test_punctuation_only(self):
        result = slugify_manual("!@#$%^&*()")
        self.assertIsNone(result)

    def test_custom_separator(self):
        result = slugify_manual("Madam, I'm Adam", separator="")
        self.assertEqual(result, "madamimadam")

    def test_preserve_casing(self):
        result = slugify_manual("StUdLy CaPs", lowercase=False)
        self.assertEqual(result, "StUdLy-CaPs")

    def test_truncate(self):
        result = slugify_manual("Call me maybe", truncate=10)
        self.assertEqual(result, "call-me")

    def test_unicode_transliteration(self):
        result = slugify_manual("你好, 世界")
        self.assertEqual(result, "ni-hao-shi-jie")

    def test_ignore_characters(self):
        result = slugify_manual("你好, 世界", ignore=["你", "好"])
        self.assertEqual(result, "你好-shi-jie")

    def test_leading_trailing_whitespace(self):
        result = slugify_manual("  foo bar  ")
        self.assertEqual(result, "foo-bar")

    def test_repeated_whitespace(self):
        result = slugify_manual("foo    bar")
        self.assertEqual(result, "foo-bar")

    def test_truncate_too_small(self):
        result = slugify_manual("foo bar", truncate=1)
        self.assertEqual(result, "")

    def test_mixed_language_input(self):
        result = slugify_manual("Hello 你好")
        self.assertEqual(result, "hello-ni-hao")

    def test_default_separator(self):
        result = slugify_manual("foo bar")
        self.assertEqual(result, "foo-bar")

    def test_no_valid_characters(self):
        result = slugify_manual("!@#$%^&*()", ignore="")
        self.assertIsNone(result)

    def test_ignore_list(self):
        result = slugify_manual("foo!bar", ignore=["!"])
        self.assertEqual(result, "foo!bar")

    def test_truncate_without_breaking_words(self):
        result = slugify_manual("foo bar baz", truncate=7)
        self.assertEqual(result, "foo-bar")

    def test_lowercase_default(self):
        result = slugify_manual("FOO BAR")
        self.assertEqual(result, "foo-bar")

    def test_ignore_none(self):
        result = slugify_manual("foo!bar", ignore=None)
        self.assertEqual(result, "foobar")

    def test_truncate_exact_length(self):
        result = slugify_manual("foo bar", truncate=7)
        self.assertEqual(result, "foo-bar")

    def test_truncate_longer_than_input(self):
        result = slugify_manual("foo bar", truncate=20)
        self.assertEqual(result, "foo-bar")

    def test_ignore_empty_list(self):
        result = slugify_manual("foo!bar", ignore=[])
        self.assertEqual(result, "foobar")

    def test_ignore_multiple_characters(self):
        result = slugify_manual("foo!bar#baz", ignore=["!", "#"])
        self.assertEqual(result, "foo!bar#baz")

    def test_truncate_zero(self):
        result = slugify_manual("foo bar", truncate=0)
        self.assertEqual(result, "")

    def test_truncate_negative(self):
        result = slugify_manual("foo bar", truncate=-1)
        self.assertEqual(result, "foo-bar")

    def test_ignore_non_string(self):
        result = slugify_manual("foo!bar", ignore=123)
        self.assertEqual(result, "foobar")

    def test_separator_non_string(self):
        result = slugify_manual("foo bar", separator=123)
        self.assertEqual(result, "foo123bar")

    def test_lowercase_non_boolean(self):
        result = slugify_manual("FOO BAR", lowercase=123)
        self.assertEqual(result, "foo-bar")

    def test_truncate_non_integer(self):
        result = slugify_manual("foo bar", truncate="abc")
        self.assertEqual(result, "foo-bar")

    def test_ignore_non_iterable(self):
        result = slugify_manual("foo!bar", ignore=123)
        self.assertEqual(result, "foobar")

    def test_separator_multiple_characters(self):
        result = slugify_manual("foo bar", separator="--")
        self.assertEqual(result, "foo--bar")

    def test_ignore_case_sensitive(self):
        result = slugify_manual("FOO!bar", ignore=["!"])
        self.assertEqual(result, "foo!bar")

    def test_truncate_with_ignore(self):
        result = slugify_manual("foo!bar", truncate=5, ignore=["!"])
        self.assertEqual(result, "foo!b")

    def test_separator_with_ignore(self):
        result = slugify_manual("foo!bar", separator="--", ignore=["!"])
        self.assertEqual(result, "foo!--bar")

    def test_lowercase_with_ignore(self):
        result = slugify_manual("FOO!bar", lowercase=False, ignore=["!"])
        self.assertEqual(result, "FOO!bar")

    def test_truncate_with_separator(self):
        result = slugify_manual("foo bar", truncate=5, separator="--")
        self.assertEqual(result, "foo")

    def test_truncate_with_lowercase(self):
        result = slugify_manual("FOO BAR", truncate=5, lowercase=True)
        self.assertEqual(result, "foo")

    def test_truncate_with_separator_and_lowercase(self):
        result = slugify_manual("FOO BAR", truncate=5, separator="--", lowercase=True)
        self.assertEqual(result, "foo")

    def test_truncate_with_ignore_and_separator(self):
        result = slugify_manual("foo!bar", truncate=5, ignore=["!"], separator="--")
        self.assertEqual(result, "foo!b")

    def test_truncate_with_ignore_and_lowercase(self):
        result = slugify_manual("FOO!bar", truncate=5, ignore=["!"], lowercase=True)
        self.assertEqual(result, "foo!b")

    def test_truncate_with_ignore_separator_and_lowercase(self):
        result = slugify_manual("FOO!bar", truncate=5, ignore=["!"], separator="--", lowercase=True)
        self.assertEqual(result, "foo!b")

    def test_truncate_with_all_options(self):
        result = slugify_manual("FOO!bar", truncate=5, ignore=["!"], separator="--", lowercase=True)
        self.assertEqual(result, "foo!b")

    def test_truncate_with_all_options_longer_input(self):
        result = slugify_manual("FOO!bar baz", truncate=10, ignore=["!"], separator="--", lowercase=True)
        self.assertEqual(result, "foo!bar--b")

    def test_truncate_with_all_options_exact_length(self):
        result = slugify_manual("FOO!bar", truncate=7, ignore=["!"], separator="--", lowercase=True)
        self.assertEqual(result, "foo!bar")

    def test_truncate_with_all_options_longer_truncate(self):
        result = slugify_manual("FOO!bar", truncate=20, ignore=["!"], separator="--", lowercase=True)
        self.assertEqual(result, "foo!bar")

    def test_truncate_with_all_options_zero_truncate(self):
        result = slugify_manual("FOO!bar", truncate=0, ignore=["!"], separator="--", lowercase=True)
        self.assertEqual(result, "")

    def test_truncate_with_all_options_negative_truncate(self):
        result = slugify_manual("FOO!bar", truncate=-1, ignore=["!"], separator="--", lowercase=True)
        self.assertEqual(result, "foo!bar")

    def test_truncate_with_all_options_non_integer_truncate(self):
        result = slugify_manual("FOO!bar", truncate="abc", ignore=["!"], separator="--", lowercase=True)
        self.assertEqual(result, "foo!bar")

    def test_truncate_with_all_options_non_string_separator(self):
        result = slugify_manual("FOO!bar", truncate=5, ignore=["!"], separator=123, lowercase=True)
        self.assertEqual(result, "foo!b")

    def test_truncate_with_all_options_non_boolean_lowercase(self):
        result = slugify_manual("FOO!bar", truncate=5, ignore=["!"], separator="--", lowercase=123)
        self.assertEqual(result, "foo!b")

    def test_truncate_with_all_options_non_iterable_ignore(self):
        result = slugify_manual("FOO!bar", truncate=5, ignore=123, separator="--", lowercase=True)
        self.assertEqual(result, "foob")

    def test_truncate_with_all_options_empty_ignore(self):
        result = slugify_manual("FOO!bar", truncate=5, ignore=[], separator="--", lowercase=True)
        self.assertEqual(result, "foob")

    def test_truncate_with_all_options_multiple_ignore(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=["!", "#"], separator="--", lowercase=True)
        self.assertEqual(result, "foo!bar#ba")

    def test_truncate_with_all_options_case_sensitive_ignore(self):
        result = slugify_manual("FOO!bar", truncate=5, ignore=["!"], separator="--", lowercase=False)
        self.assertEqual(result, "FOO!b")

    def test_truncate_with_all_options_multiple_characters_separator(self):
        result = slugify_manual("FOO!bar", truncate=5, ignore=["!"], separator="---", lowercase=True)
        self.assertEqual(result, "foo!b")

    def test_truncate_with_all_options_multiple_characters_separator_and_ignore(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=["!", "#"], separator="---", lowercase=True)
        self.assertEqual(result, "foo!bar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_lowercase(self):
        result = slugify_manual("FOO!bar", truncate=5, ignore=["!"], separator="---", lowercase=True)
        self.assertEqual(result, "foo!b")

    def test_truncate_with_all_options_multiple_characters_separator_and_case_sensitive_ignore(self):
        result = slugify_manual("FOO!bar", truncate=5, ignore=["!"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!b")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=["!", "#"], separator="---", lowercase=True)
        self.assertEqual(result, "foo!bar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_longer_input(self):
        result = slugify_manual("FOO!bar#baz", truncate=20, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#baz")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_exact_length(self):
        result = slugify_manual("FOO!bar#baz", truncate=11, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#baz")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_zero_truncate(self):
        result = slugify_manual("FOO!bar#baz", truncate=0, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_negative_truncate(self):
        result = slugify_manual("FOO!bar#baz", truncate=-1, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#baz")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_non_integer_truncate(self):
        result = slugify_manual("FOO!bar#baz", truncate="abc", ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#baz")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_non_string_separator(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=["!", "#"], separator=123, lowercase=False)
        self.assertEqual(result, "FOO!bar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_non_boolean_lowercase(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=["!", "#"], separator="---", lowercase=123)
        self.assertEqual(result, "FOO!bar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_non_iterable_ignore(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=123, separator="---", lowercase=False)
        self.assertEqual(result, "FOObar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_empty_ignore(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=[], separator="---", lowercase=False)
        self.assertEqual(result, "FOObar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_ignore(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_case_sensitive_ignore(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_ignore(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_lowercase(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_case_sensitive_ignore(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_longer_input(self):
        result = slugify_manual("FOO!bar#baz", truncate=20, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#baz")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_exact_length(self):
        result = slugify_manual("FOO!bar#baz", truncate=11, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#baz")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_zero_truncate(self):
        result = slugify_manual("FOO!bar#baz", truncate=0, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_negative_truncate(self):
        result = slugify_manual("FOO!bar#baz", truncate=-1, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#baz")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_non_integer_truncate(self):
        result = slugify_manual("FOO!bar#baz", truncate="abc", ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#baz")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_non_string_separator(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=["!", "#"], separator=123, lowercase=False)
        self.assertEqual(result, "FOO!bar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_non_boolean_lowercase(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=["!", "#"], separator="---", lowercase=123)
        self.assertEqual(result, "FOO!bar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_non_iterable_ignore(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=123, separator="---", lowercase=False)
        self.assertEqual(result, "FOObar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_empty_ignore(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=[], separator="---", lowercase=False)
        self.assertEqual(result, "FOObar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_ignore(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_case_sensitive_ignore(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_ignore(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_lowercase(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_case_sensitive_ignore(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive(self):
        result = slugify_manual("FOO!bar#baz", truncate=10, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#ba")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_longer_input(self):
        result = slugify_manual("FOO!bar#baz", truncate=20, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#baz")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_exact_length(self):
        result = slugify_manual("FOO!bar#baz", truncate=11, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#baz")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_zero_truncate(self):
        result = slugify_manual("FOO!bar#baz", truncate=0, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_negative_truncate(self):
        result = slugify_manual("FOO!bar#baz", truncate=-1, ignore=["!", "#"], separator="---", lowercase=False)
        self.assertEqual(result, "FOO!bar#baz")

    def test_truncate_with_all_options_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_characters_separator_and_multiple_ignore_case_sensitive_multiple_char