from typing import TypedDict

import pytest

from . import Solution


class InputDict(TypedDict):
    s: str
    t: str


class CaseDict(TypedDict):
    input: InputDict
    expected: bool


test_cases: list[CaseDict] = [
    {
        "input": {
            "s": "abc",
            "t": "ahbgdc",
        },
        "expected": True,
    },
    {
        "input": {
            "s": "axc",
            "t": "ahbgdc",
        },
        "expected": False,
    },
]


@pytest.mark.parametrize(
    'test_case',
    test_cases,
)
def test_solution(test_case: CaseDict):
    result = Solution().isSubsequence(**test_case["input"])
    assert result == test_case["expected"]
