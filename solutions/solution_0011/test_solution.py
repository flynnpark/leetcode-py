from typing import List, TypedDict

import pytest

from . import Solution


class InputDict(TypedDict):
    height: List[int]


class CaseDict(TypedDict):
    input: InputDict
    expected: int


test_cases: list[CaseDict] = [
    {
        "input": {
            "height": [1, 8, 6, 2, 5, 4, 8, 3, 7],
        },
        "expected": 49,
    },
    {
        "input": {
            "height": [1, 1],
        },
        "expected": 1,
    },
]


@pytest.mark.parametrize(
    'test_case',
    test_cases,
)
def test_solution(test_case: CaseDict):
    result = Solution().maxArea(**test_case["input"])
    assert result == test_case["expected"]
