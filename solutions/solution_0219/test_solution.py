from typing import TypedDict

import pytest

from . import Solution


class InputDict(TypedDict):
    nums: list[int]
    k: int


class CaseDict(TypedDict):
    input: InputDict
    expected: bool


test_cases: list[CaseDict] = [
    {
        'input': {
            'nums': [1, 2, 3, 1],
            'k': 3,
        },
        'expected': True,
    },
    {
        'input': {
            'nums': [1, 0, 1, 1],
            'k': 1,
        },
        'expected': True,
    },
    {
        'input': {
            'nums': [1, 2, 3, 1, 2, 3],
            'k': 2,
        },
        'expected': False,
    },
]


@pytest.mark.parametrize(
    'test_case',
    test_cases,
)
def test_solution(test_case: CaseDict):
    result = Solution().containsNearbyDuplicate(**test_case['input'])
    assert result == test_case['expected']
