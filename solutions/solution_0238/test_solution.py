from typing import TypedDict

from . import Solution


class CaseDict(TypedDict):
    input: list[int]
    expected: list[int]


test_cases: list[CaseDict] = [
    {
        'input': [1, 2, 3, 4],
        'expected': [24, 12, 8, 6],
    },
    {
        'input': [-1, 1, 0, -3, 3],
        'expected': [0, 0, 9, 0, 0],
    },
]


def test_solution():
    for test_case in test_cases:
        actual = Solution().productExceptSelf(test_case['input'])
        expected = test_case['expected']
        assert actual == expected
