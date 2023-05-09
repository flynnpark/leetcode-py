from typing import TypedDict

from . import Solution


class CaseDict(TypedDict):
    input: list[int]
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': [7, 1, 5, 3, 6, 4],
        'expected': 5,
    },
    {
        'input': [7, 6, 4, 3, 1],
        'expected': 0,
    },
]


def test_solution():
    for test_case in test_cases:
        actual = Solution().maxProfit(test_case['input'])
        expected = test_case['expected']
        assert actual == expected
