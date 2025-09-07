import pytest

from app import safe_divide


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 2, 5.0),
        (-9, 3, -3.0),
        (7.5, 2.5, 3.0),
    ],
)
def test_safe_divide_normal(a, b, expected):
    assert safe_divide(a, b) == expected


def test_safe_divide_zero_with_default():
    assert safe_divide(1, 0, default=0.0) == 0.0


def test_safe_divide_zero_raises_without_default():
    with pytest.raises(ZeroDivisionError):
        safe_divide(1, 0)
