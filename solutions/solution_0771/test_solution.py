from typing import TypedDict

from . import Solution


class CaseDict(TypedDict):
    input: dict[str, str]
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': {
            'jewels': 'aA',
            'stones': 'aAAbbbb',
        },
        'expected': 3,
    },
    {
        'input': {
            'jewels': 'z',
            'stones': 'ZZ',
        },
        'expected': 0,
    },
]


def test_solution():
    for test_case in test_cases:
        assert Solution().numJewelsInStones(**test_case['input']) == test_case['expected']
