from typing import List, TypedDict

import pytest

from . import Solution


class InputDict(TypedDict):
    nums: List[int]
    k: int


class CaseDict(TypedDict):
    input: InputDict
    expected: int


test_cases: list[CaseDict] = [
    {
        "input": {
            "nums": [1, 2, 3, 4],
            "k": 5,
        },
        "expected": 2,
    },
    {
        "input": {
            "nums": [3, 1, 3, 4, 3],
            "k": 6,
        },
        "expected": 1,
    },
]


@pytest.mark.parametrize(
    'test_case',
    test_cases,
)
def test_solution(test_case: CaseDict):
    result = Solution().maxOperations(**test_case["input"])
    assert result == test_case["expected"]
