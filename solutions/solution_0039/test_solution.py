from typing import TypedDict

from . import Solution


class InputDict(TypedDict):
    candidates: list[int]
    target: int


class CaseDict(TypedDict):
    input: InputDict
    expected: list[list[int]]


test_cases: list[CaseDict] = [
    {
        'input': {
            'candidates': [2, 3, 6, 7],
            'target': 7,
        },
        'expected': [[2, 2, 3], [7]],
    },
    {
        'input': {
            'candidates': [2, 3, 5],
            'target': 8,
        },
        'expected': [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
    },
    {'input': {'candidates': [2], 'target': 1}, 'expected': []},
]


def test_solution():
    for test_case in test_cases:
        input = test_case['input']
        assert test_case['expected'] == Solution().combinationSum(**input)
