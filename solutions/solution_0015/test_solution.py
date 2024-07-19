from typing import TypedDict

from . import Solution


class CaseDict(TypedDict):
    input: list[int]
    expected: list[list[int]]


test_cases: list[CaseDict] = [
    {'input': [-1, 0, 1, 2, -1, -4], 'expected': [[-1, -1, 2], [-1, 0, 1]]},
    {'input': [], 'expected': []},
    {'input': [0], 'expected': []},
]


def test_solution():
    for test_case in test_cases:
        actual_result = Solution().threeSum(test_case['input'])
        assert actual_result == test_case['expected']
