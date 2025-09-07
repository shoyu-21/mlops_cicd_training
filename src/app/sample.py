from __future__ import annotations


def add(a: float, b: float) -> float:
    """Return the sum of two numbers.

    Examples
    --------
    >>> add(1, 2)
    3
    """

    return a + b


def is_palindrome(text: str) -> bool:
    """Return True if `text` reads the same forwards and backwards.

    Ignores casing and non-alphanumeric characters.
    """

    normalized = "".join(ch.lower() for ch in text if ch.isalnum())
    return normalized == normalized[::-1]
