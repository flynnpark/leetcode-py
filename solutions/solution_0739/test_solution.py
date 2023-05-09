from typing import TypedDict

from . import Solution

CaseDict = TypedDict("CaseDict", {"input": list[int], "expected": list[int]})


test_cases: list[CaseDict] = [
    {
        "input": [73, 74, 75, 71, 69, 72, 76, 73],
        "expected": [1, 1, 4, 2, 1, 1, 0, 0],
    },
    {"input": [30, 40, 50, 60], "expected": [1, 1, 1, 0]},
    {"input": [30, 60, 90], "expected": [1, 1, 0]},
]


def test_solution():
    for test_case in test_cases:
        assert Solution().dailyTemperatures(test_case["input"]) == test_case["expected"]
