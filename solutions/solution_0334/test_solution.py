from typing import TypedDict

from . import Solution


class InputDict(TypedDict):
    nums: list[int]


class CaseDict(TypedDict):
    input: InputDict
    expected: bool


test_cases: list[CaseDict] = [
    {
        'input': {
            'nums': [1, 2, 3, 4, 5],
        },
        'expected': True,
    },
    {
        'input': {
            'nums': [5, 4, 3, 2, 1],
        },
        'expected': False,
    },
    {
        'input': {
            'nums': [2, 1, 5, 0, 4, 6],
        },
        'expected': True,
    },
]


def test_solution():
    for test_case in test_cases:
        result = Solution().increasingTriplet(**test_case['input'])
        assert result == test_case['expected']
