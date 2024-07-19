from typing import TypedDict

from . import Solution


class CaseDict(TypedDict):
    input: int
    expected: bool


test_cases: list[CaseDict] = [
    {'input': 121, 'expected': True},
    {'input': -121, 'expected': False},
    {'input': 10, 'expected': False},
    {'input': -101, 'expected': False},
]


def test_solution():
    for test_case in test_cases:
        actual_result = Solution().isPalindrome(test_case['input'])
        assert actual_result == test_case['expected']
