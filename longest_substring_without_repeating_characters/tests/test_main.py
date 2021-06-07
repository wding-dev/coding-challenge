import pytest

from longest_substring_without_repeating_characters.main import solution


@pytest.mark.parametrize(
    "s, expected", [
    ("happy", 3),
    ("abcabcbb", 3),
    ("pwwkew", 3),
    (" ", 1),
    ("ab", 2),
    ("abcdefg", 7),
    ("", 0),
    ("dvdf", 3),
    ("cc", 1)
])
def test_solution(s, expected):
    assert solution(s) == expected
