import pytest

from longest_substring_without_repeating_characters.main import solution


@pytest.mark.parametrize(
    "s, expected", [
    ("happy", 3),
    ("abcabcbb", 3),
    ("pwwkew", 3)
])
def test_solution(s, expected):
    assert solution(s) == expected
