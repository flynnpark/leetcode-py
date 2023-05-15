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
            "nums": [0, 1, 0, 3, 12],
        },
        "expected": [1, 3, 12, 0, 0],
    },
    {
        "input": {
            "nums": [0],
        },
        "expected": [0],
    },
]


def test_solution():
    for test_case in test_cases:
        nums = test_case['input']['nums']
        Solution().moveZeroes(**test_case["input"])
        assert nums == test_case["expected"]
