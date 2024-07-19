from typing import TypedDict

from . import Solution


class CaseDict(TypedDict):
    input: str
    expected: int


test_cases: list[CaseDict] = [
    {'input': 'III', 'expected': 3},
    {'input': 'IV', 'expected': 4},
    {'input': 'IX', 'expected': 9},
    {'input': 'LVIII', 'expected': 58},
    {'input': 'MCMXCIV', 'expected': 1994},
]


def test_solution():
    for test_case in test_cases:
        actual_result = Solution().romanToInt(test_case['input'])
        assert actual_result == test_case['expected']
