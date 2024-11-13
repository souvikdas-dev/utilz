# test_string_utils.py
import unittest

from utilz.string_utils import capitalize_words, is_palindrome, reverse_string


class TestStringUtils(unittest.TestCase):
    def test_capitalize_words(self):
        self.assertEqual(capitalize_words("hello world"), "Hello World")

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertFalse(is_palindrome("hello"))


if __name__ == "__main__":
    unittest.main()
