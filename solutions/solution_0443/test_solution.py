from typing import TypedDict

from . import Solution


class InputDict(TypedDict):
    chars: list[str]


class CaseDict(TypedDict):
    input: InputDict
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': {
            'chars': ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
        },
        'expected': 6,
    },
    {
        'input': {
            'chars': ['a'],
        },
        'expected': 1,
    },
    {
        'input': {
            'chars': ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
        },
        'expected': 4,
    },
]


def test_solution():
    for test_case in test_cases:
        result = Solution().compress(**test_case['input'])
        assert result == test_case['expected']
