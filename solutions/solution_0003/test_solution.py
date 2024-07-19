from typing import TypedDict

from . import Solution


class CaseDict(TypedDict):
    input: str
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': 'abcabcbb',
        'expected': 3,
    },
    {
        'input': 'bbbbb',
        'expected': 1,
    },
    {
        'input': 'pwwkew',
        'expected': 3,
    },
]


def test_solution():
    for test_case in test_cases:
        assert Solution().lengthOfLongestSubstring(test_case['input']) == test_case['expected']
