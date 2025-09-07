import json
from pathlib import Path

import pytest

from app.sample import add, is_palindrome


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (-1, 1, 0),
        (2.5, 0.5, 3.0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("racecar", True),
        ("RaceCar", True),
        ("A man, a plan, a canal: Panama!", True),
        ("not a palindrome", False),
    ],
)
def test_is_palindrome(text, expected):
    assert is_palindrome(text) is expected


def test_with_tmp_path_fixture(tmp_path: Path):
    """Show using pytest's built-in tmp_path fixture."""

    data = {"result": add(2, 3), "pal": is_palindrome("level")}
    out = tmp_path / "result.json"
    out.write_text(json.dumps(data))

    loaded = json.loads(out.read_text())
    assert loaded == {"result": 5, "pal": True}
