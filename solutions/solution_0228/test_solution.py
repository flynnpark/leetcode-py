from typing import TypedDict

from . import Solution


class CaseInput(TypedDict):
    nums: list[int]


class CaseDict(TypedDict):
    input: CaseInput
    expected: list[str]


test_cases: list[CaseDict] = [
    {
        'input': {'nums': [0, 1, 2, 4, 5, 7]},
        'expected': ['0->2', '4->5', '7'],
    },
    {
        'input': {'nums': [0, 2, 3, 4, 6, 8, 9]},
        'expected': ['0', '2->4', '6', '8->9'],
    },
]


def test_solution():
    for test_case in test_cases:
        assert Solution().summaryRanges(**test_case['input']) == test_case['expected']
