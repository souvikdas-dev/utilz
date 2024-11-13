# test_file_utils.py
# import os
import unittest

from utilz.file_utils import file_exists, read_file, write_to_file


class TestFileUtils(unittest.TestCase):
    def test_write_and_read_file(self):
        write_to_file("test.txt", "Hello, world!")
        self.assertTrue(file_exists("test.txt"))
        self.assertEqual(read_file("test.txt"), "Hello, world!")

    def test_file_exists(self):
        self.assertTrue(file_exists("test.txt"))
        self.assertFalse(file_exists("non_existent.txt"))


if __name__ == "__main__":
    unittest.main()
