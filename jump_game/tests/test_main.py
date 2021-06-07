import pytest

from jump_game.main import solution


@pytest.mark.parametrize(
    "nums, expected", [
    ([2,3,1,1,4], True),
    ([3,2,1,0,4], False),
    ([1,0,0,3,0,4], False),
    ([1,3,0,1,2,0,4,0,0,1], True)
])
def test_solution(nums, expected):
    assert solution(nums) == expected
