from typing import TypedDict

from . import Solution


class CaseDict(TypedDict):
    input: int
    expected: int


test_cases: list[CaseDict] = [
    {'input': 123, 'expected': 321},
    {'input': -123, 'expected': -321},
    {'input': 120, 'expected': 21},
    {'input': 0, 'expected': 0},
]


def test_solution():
    for test_case in test_cases:
        actual_result = Solution().reverse(test_case['input'])
        assert actual_result == test_case['expected']
