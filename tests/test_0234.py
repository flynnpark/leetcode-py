from typing import List, TypedDict
from solutions.solution_0234 import Solution


class CaseDict(TypedDict):
    input: List[int]
    expected: bool


test_cases: List[CaseDict] = [
    {"input": [1, 2, 2, 1], "expected": True},
    {"input": [1, 2], "expected": False},
]


def test_solution():
    for test_case in test_cases:
        actual_result = Solution().isPalindrome(test_case["input"])
        assert actual_result == test_case["expected"]
