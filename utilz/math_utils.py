# Utility functions for math

# math_utils.py

import math


def gcd(a, b):
    """Return the greatest common divisor of a and b."""
    return math.gcd(a, b)


def lcm(a, b):
    """Return the least common multiple of a and b."""
    return abs(a * b) // gcd(a, b)
