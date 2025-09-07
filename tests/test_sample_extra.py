import pytest

from app.sample import add, is_palindrome


def test_add_large_numbers():
    assert add(10_000_000, 23_456_789) == 33_456_789


def test_add_raises_type_error_on_mixed_types():
    with pytest.raises(TypeError):
        add("1", 2)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "text,expected",
    [
        ("", True),  # empty is trivially palindrome
        ("   ", True),  # only spaces
        ("!!!", True),  # only punctuation
        ("12321", True),
        ("12345", False),
        ("Was it a car or a cat I saw?", True),
        ("No 'x' in Nixon", True),
        ("たけやぶやけた", True),  # Japanese palindrome
    ],
)
def test_is_palindrome_various_cases(text: str, expected: bool):
    assert is_palindrome(text) is expected
