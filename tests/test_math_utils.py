# test_math_utils.py
import unittest

from utilz.math_utils import factorial, gcd, is_prime


class TestMathUtils(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

    def test_is_prime(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(10))

    def test_gcd(self):
        self.assertEqual(gcd(54, 24), 6)
        self.assertEqual(gcd(101, 103), 1)


if __name__ == "__main__":
    unittest.main()
