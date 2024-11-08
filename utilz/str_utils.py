# Utility functions for strings

# str_utils.py


def capitalize_words(text):
    """Capitalize the first letter of each word in a string."""
    return " ".join(word.capitalize() for word in text.split())


def truncate(text, length=10):
    """Truncate the string to a certain length."""
    return text[:length] + ("..." if len(text) > length else "")
