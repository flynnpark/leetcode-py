from typing import TypedDict

from . import Solution


class CaseInput(TypedDict):
    nums: list[int]
    target: int


class CaseDict(TypedDict):
    input: CaseInput
    expected: int


test_cases: list[CaseDict] = [
    {'input': {'nums': [1, 3, 5, 6], 'target': 5}, 'expected': 2},
    {'input': {'nums': [1, 3, 5, 6], 'target': 2}, 'expected': 1},
    {'input': {'nums': [1, 3, 5, 6], 'target': 7}, 'expected': 4},
    {'input': {'nums': [1, 3, 5, 6], 'target': 0}, 'expected': 0},
    {'input': {'nums': [1], 'target': 0}, 'expected': 0},
]


def test_solution():
    for test_case in test_cases:
        actual_result = Solution().searchInsert(
            nums=test_case['input']['nums'],
            target=test_case['input']['target'],
        )
        assert actual_result == test_case['expected']
