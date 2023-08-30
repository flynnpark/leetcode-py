from typing import TypedDict

import pytest

from . import Solution


class InputDict(TypedDict):
    gain: list[int]


class CaseDict(TypedDict):
    input: InputDict
    expected: int


test_cases: list[CaseDict] = [
    {
        'input': {
            'gain': [-5, 1, 5, 0, -7],
        },
        'expected': 1,
    },
    {
        'input': {
            'gain': [-4, -3, -2, -1, 4, 3, 2],
        },
        'expected': 0,
    },
]


@pytest.mark.parametrize(
    'test_case',
    test_cases,
)
def test_solution(test_case: CaseDict):
    result = Solution().largestAltitude(**test_case['input'])
    assert result == test_case['expected']
