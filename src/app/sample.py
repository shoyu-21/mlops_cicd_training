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


def clamp(x: float, min_value: float, max_value: float) -> float:
    """Clamp `x` into the inclusive range [`min_value`, `max_value`].

    Raises ValueError when `min_value` is greater than `max_value`.
    """

    if min_value > max_value:
        raise ValueError("min_value cannot be greater than max_value")
    if x < min_value:
        return min_value
    if x > max_value:
        return max_value
    return x
