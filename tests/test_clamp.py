import math
import pytest

from app import clamp


@pytest.mark.parametrize(
    "x,low,high,expected",
    [
        (-10, 0, 5, 0),  # below
        (0, 0, 5, 0),  # at lower bound
        (2.5, 0, 5, 2.5),  # inside
        (5, 0, 5, 5),  # at upper bound
        (10, 0, 5, 5),  # above
        (math.inf, -1, 1, 1),
        (-math.inf, -1, 1, -1),
    ],
)
def test_clamp_values(x, low, high, expected):
    assert clamp(x, low, high) == expected


def test_clamp_raises_on_invalid_range():
    with pytest.raises(ValueError):
        clamp(1, 5, 0)
