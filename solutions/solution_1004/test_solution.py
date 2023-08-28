from typing import TypedDict

import pytest

from . import Solution


class InputDict(TypedDict):
    nums: list[int]
    k: int


class CaseDict(TypedDict):
    input: InputDict
    expected: int


test_cases: list[CaseDict] = [
    {
        "input": {
            'nums': [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],
            'k': 2,
        },
        "expected": 6,
    },
    {
        "input": {
            'nums': [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
            'k': 3,
        },
        "expected": 10,
    },
]


@pytest.mark.parametrize(
    'test_case',
    test_cases,
)
def test_solution(test_case: CaseDict):
    result = Solution().longestOnes(**test_case["input"])
    assert result == test_case["expected"]
