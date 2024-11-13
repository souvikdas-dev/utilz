# Utility functions for math

# math_utils.py


def gcd(a: int, b: int) -> int:
    """
    Returns the greatest common divisor of a and b using Euclid's algorithm.
    Example: gcd(54, 24) -> 6
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Return the least common multiple of a and b."""
    return abs(a * b) // gcd(a, b)


def factorial(n: int) -> int:
    """
    Returns the factorial of a number.
    Example: 5 -> 120
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)


def is_prime(n: int) -> bool:
    """
    Checks if a number is prime.
    Example: 7 -> True
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
