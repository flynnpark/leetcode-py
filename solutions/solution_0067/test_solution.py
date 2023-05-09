from typing import List, TypedDict

from . import Solution


class CaseInput(TypedDict):
    a: str
    b: str


class CastDict(TypedDict):
    input: CaseInput
    expected: str


test_cases: List[CastDict] = [
    {"input": {"a": "11", "b": "1"}, "expected": "100"},
    {"input": {"a": "1010", "b": "1011"}, "expected": "10101"},
]


def test_solution():
    for test_case in test_cases:
        actual_result = Solution().addBinary(**test_case["input"])
        assert actual_result == test_case["expected"]
