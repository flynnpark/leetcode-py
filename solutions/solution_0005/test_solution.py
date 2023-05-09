from typing import List, TypedDict

from . import Solution

CaseDict = TypedDict('CaseDict', {'input': str, 'expected': List[str]})


test_cases: List[CaseDict] = [
    {"input": "babad", "expected": ["bab", "aba"]},
    {"input": "cbbd", "expected": ["bb"]},
    {"input": "a", "expected": ["a"]},
    {"input": "ac", "expected": ["a", "c"]},
]


def test_solution():
    for test_case in test_cases:
        actual_result = Solution().longestPalindrome(test_case["input"])
        assert actual_result in test_case["expected"]
