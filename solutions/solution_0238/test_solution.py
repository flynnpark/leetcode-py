from typing import List, TypedDict

from . import Solution


class InputDict(TypedDict):
    nums: List[int]


class CaseDict(TypedDict):
    input: InputDict
    expected: List[int]


test_cases: list[CaseDict] = [
    {
        "input": {
            "nums": [1, 2, 3, 4],
        },
        "expected": [24, 12, 8, 6],
    },
    {
        "input": {
            "nums": [-1, 1, 0, -3, 3],
        },
        "expected": [0, 0, 9, 0, 0],
    },
]


def test_solution():
    for test_case in test_cases:
        result = Solution().productExceptSelf(**test_case["input"])
        assert result == test_case["expected"]
