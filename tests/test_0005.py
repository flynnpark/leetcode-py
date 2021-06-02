from typing import List, TypedDict

from solutions.solution_0005 import Solution


class TestCase(TypedDict):
    input: str
    expected: str


test_cases: List[TestCase] = [
    {"input": "babad", "expected": "bab"},
    {"input": "cbbd", "expected": "bb"},
    {"input": "a", "expected": "a"},
    {"input": "ac", "expected": "a"},
]


def test_solution():
    for test_case in test_cases:
        actual_result = Solution().longestPalindrome(test_case["input"])
        assert actual_result == test_case["expected"]
