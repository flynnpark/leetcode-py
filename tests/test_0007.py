from typing import List, TypedDict
from solutions.solution_0007 import Solution


class CaseDict(TypedDict):
    input: int
    expected: int


test_cases: List[CaseDict] = [
    {"input": 123, "expected": 321},
    {"input": -123, "expected": -321},
    {"input": 120, "expected": 21},
    {"input": 0, "expected": 0},
]


def test_solution():
    for test_case in test_cases:
        actual_result = Solution().reverse(test_case["input"])
        assert actual_result in test_case["expected"]
