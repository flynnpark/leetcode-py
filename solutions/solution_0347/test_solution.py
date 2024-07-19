from typing import TypedDict

from . import Solution


class InputDict(TypedDict):
    nums: list[int]
    k: int


class CaseDict(TypedDict):
    input: InputDict
    expected: list[int]


test_cases: list[CaseDict] = [
    {
        'input': {
            'nums': [1, 1, 1, 2, 2, 3],
            'k': 2,
        },
        'expected': [1, 2],
    },
    {
        'input': {
            'nums': [1],
            'k': 1,
        },
        'expected': [1],
    },
]


def test_solution():
    for test_case in test_cases:
        assert Solution().topKFrequent(**test_case['input']) == test_case['expected']
