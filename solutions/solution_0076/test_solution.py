from typing import TypedDict

import pytest

from . import Solution


class InputDict(TypedDict):
    s: str
    t: str


class CaseDict(TypedDict):
    input: InputDict
    expected: str


test_cases: list[CaseDict] = [
    {
        'input': {
            's': 'ADOBECODEBANC',
            't': 'ABC',
        },
        'expected': 'BANC',
    },
    {
        'input': {
            's': 'a',
            't': 'a',
        },
        'expected': 'a',
    },
    {
        'input': {
            's': 'a',
            't': 'aa',
        },
        'expected': '',
    },
]


@pytest.mark.parametrize(
    'test_case',
    test_cases,
)
def test_solution(test_case: CaseDict):
    result = Solution().minWindow(**test_case['input'])
    assert result == test_case['expected']
