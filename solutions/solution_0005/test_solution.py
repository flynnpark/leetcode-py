from typing import TypedDict

from . import Solution


class CaseDict(TypedDict):
    input: str
    expected: list[str]


test_cases: list[CaseDict] = [
    {'input': 'babad', 'expected': ['bab', 'aba']},
    {'input': 'cbbd', 'expected': ['bb']},
    {'input': 'a', 'expected': ['a']},
    {'input': 'ac', 'expected': ['a', 'c']},
]


def test_solution():
    for test_case in test_cases:
        actual_result = Solution().longestPalindrome(test_case['input'])
        assert actual_result in test_case['expected']
