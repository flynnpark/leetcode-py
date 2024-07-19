from typing import TypedDict

from . import Solution


class CaseDict(TypedDict):
    input: str
    expected: bool


test_cases: list[CaseDict] = [
    {'input': '()', 'expected': True},
    {'input': '()[]{}', 'expected': True},
    {'input': '(]', 'expected': False},
    {'input': '([)]', 'expected': False},
    {'input': '{[]}', 'expected': True},
    {'input': '(', 'expected': False},
]


def test_solution():
    for test_case in test_cases:
        actual_result = Solution().isValid(test_case['input'])
        assert actual_result == test_case['expected']
