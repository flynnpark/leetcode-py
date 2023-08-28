from typing import TypedDict

import pytest

from . import Solution


class InputDict(TypedDict):
    nums: list[int]


class CaseDict(TypedDict):
    input: InputDict
    expected: int


test_cases: list[CaseDict] = [
    {
        "input": {
            'nums': [1, 1, 0, 1],
        },
        "expected": 3,
    },
    {
        "input": {
            'nums': [0, 1, 1, 1, 0, 1, 1, 0, 1],
        },
        "expected": 5,
    },
    {
        "input": {
            'nums': [1, 1, 1],
        },
        "expected": 2,
    },
]


@pytest.mark.parametrize(
    'test_case',
    test_cases,
)
def test_solution(test_case: CaseDict):
    result = Solution().longestSubarray(**test_case["input"])
    assert result == test_case["expected"]
