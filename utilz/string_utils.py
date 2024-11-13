# Utility functions for strings

# str_utils.py


def capitalize_words(text: str) -> str:
    """
    Capitalizes the first letter of each word in a string.
    Example: 'hello world' -> 'Hello World'
    """
    return " ".join(word.capitalize() for word in text.split())


def truncate(text: str, length: int = 10) -> str:
    """Truncate the string to a certain length.
    Example: 'hello world' -> 'Hello Worl'

    Args:
        text (str):
        length (int, optional): Defaults to 10.

    Returns:
        str:
    """
    return text[:length] + ("..." if len(text) > length else "")


def reverse_string(text: str) -> str:
    """
    Reverses the given string.
    Example: 'hello' -> 'olleh'
    """
    return text[::-1]


def is_palindrome(text: str) -> bool:
    """
    Checks if a string is a palindrome.
    Example: 'madam' -> True
    """
    clean_text = "".join(e for e in text if e.isalnum()).lower()
    return clean_text == clean_text[::-1]
