from typing import TypedDict

import pytest

from . import Solution


class InputDict(TypedDict):
    nums: list[int]


class CaseDict(TypedDict):
    input: InputDict
    expected: list[int]


test_cases: list[CaseDict] = [
    {
        'input': {
            'nums': [0, 1, 0, 3, 12],
        },
        'expected': [1, 3, 12, 0, 0],
    },
    {
        'input': {
            'nums': [0],
        },
        'expected': [0],
    },
]


@pytest.mark.parametrize(
    'test_case',
    test_cases,
)
def test_solution(test_case: CaseDict):
    nums = test_case['input']['nums']
    Solution().moveZeroes(**test_case['input'])
    assert nums == test_case['expected']
