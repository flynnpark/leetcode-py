from typing import TypedDict

import pytest

from . import Solution


class InputDict(TypedDict):
    nums: list[int]
    k: int


class CaseDict(TypedDict):
    input: InputDict
    expected: float


test_cases: list[CaseDict] = [
    CaseDict(
        input=InputDict(
            nums=[1, 12, -5, -6, 50, 3],
            k=4,
        ),
        expected=12.75000,
    ),
    CaseDict(
        input=InputDict(
            nums=[5],
            k=1,
        ),
        expected=5.00000,
    ),
]


@pytest.mark.parametrize(
    'test_case',
    test_cases,
)
def test_solution(test_case: CaseDict):
    result = Solution().findMaxAverage(**test_case['input'])
    assert result == test_case['expected']
