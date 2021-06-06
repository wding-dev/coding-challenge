import pytest

from two_sum.main import solution


@pytest.mark.parametrize(
    "num, target, expected", [
    ([2,7,11,15], 9, [0, 1]),
    ([2,1,5,3], 4, [1, 3])
])
def test_solution(num, target, expected):
    assert solution(num, target) == expected
