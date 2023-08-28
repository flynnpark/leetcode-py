from typing import TypedDict

import pytest

from . import Solution


class InputDict(TypedDict):
    s: str
    k: int


class CaseDict(TypedDict):
    input: InputDict
    expected: int


test_cases: list[CaseDict] = [
    {
        "input": {
            's': 'aeiou',
            'k': 2,
        },
        "expected": 2,
    },
    {
        "input": {
            's': 'leetcode',
            'k': 3,
        },
        "expected": 2,
    },
]


@pytest.mark.parametrize(
    'test_case',
    test_cases,
)
def test_solution(test_case: CaseDict):
    result = Solution().maxVowels(**test_case["input"])
    assert result == test_case["expected"]
