from typing import TypedDict

import pytest

from . import Solution


class InputDict(TypedDict):
    nums: list[int]


class CaseDict(TypedDict):
    input: InputDict
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': {
            'nums': [100, 4, 200, 1, 3, 2],
        },
        'expected': 4,
    },
    {
        'input': {
            'nums': [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
        },
        'expected': 9,
    },
    {
        'input': {
            'nums': [0, 3, 7, 2, 5, 8, 4, 6, 0, 1, 2, 3, 4, 5, 6, 7, 8],
        },
        'expected': 9,
    },
]


@pytest.mark.parametrize(
    'test_case',
    test_cases,
)
def test_solution(test_case: CaseDict):
    result = Solution().longestConsecutive(**test_case['input'])
    assert result == test_case['expected']
