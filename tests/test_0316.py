from typing import List, TypedDict

from solutions.solution_0316 import Solution

CaseDict = TypedDict("CaseDict", {"input": str, "expected": str})


test_cases: List[CaseDict] = [
    {
        "input": "bcabc",
        "expected": "abc",
    },
    {"input": "cbacdcbc", "expected": "acdb"},
]


def test_solution():
    for test_case in test_cases:
        result = Solution().removeDuplicateLetters(test_case["input"])
        assert result == test_case["expected"]
