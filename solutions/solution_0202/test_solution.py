from typing import TypedDict

from . import Solution


class CaseInput(TypedDict):
    n: int


class CaseDict(TypedDict):
    input: CaseInput
    expected: bool


test_cases: list[CaseDict] = [
    {
        'input': {'n': 19},
        'expected': True,
    },
    {
        'input': {'n': 2},
        'expected': False,
    },
]


def test_solution():
    for test_case in test_cases:
        assert Solution().isHappy(**test_case['input']) == test_case['expected']
