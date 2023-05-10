from typing import List, TypedDict

from . import Solution


class InputDict(TypedDict):
    candies: List[int]
    extraCandies: int


class CaseDict(TypedDict):
    input: InputDict
    expected: List[bool]


test_cases: list[CaseDict] = [
    {
        "input": {
            "candies": [2, 3, 5, 1, 3],
            "extraCandies": 3,
        },
        "expected": [True, True, True, False, True],
    },
    {
        "input": {
            "candies": [4, 2, 1, 1, 2],
            "extraCandies": 1,
        },
        "expected": [True, False, False, False, False],
    },
    {
        "input": {
            "candies": [12, 1, 12],
            "extraCandies": 10,
        },
        "expected": [True, False, True],
    },
]


def test_solution():
    for test_case in test_cases:
        result = Solution().kidsWithCandies(**test_case["input"])
        assert result == test_case["expected"]
