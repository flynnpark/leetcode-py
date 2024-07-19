from typing import TypedDict

from . import Solution


class CaseDict(TypedDict):
    input: list[str]
    expected: str


test_cases: list[CaseDict] = [
    {'input': ['flower', 'flow', 'flight'], 'expected': 'fl'},
    {'input': ['dog', 'racecar', 'car'], 'expected': ''},
    {'input': ['cir', 'car'], 'expected': 'c'},
]


def test_solution():
    for test_case in test_cases:
        actual_result = Solution().longestCommonPrefix(test_case['input'])
        assert actual_result == test_case['expected']
