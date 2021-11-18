from typing import List, TypedDict

from solutions.solution_0029 import Solution


class InputDict(TypedDict):
    dividend: int
    divisor: int


class CaseDict(TypedDict):
    input: InputDict
    expected: int


test_cases: List[CaseDict] = [
    {
        "input": {"dividend": 10, "divisor": 3},
        "expected": 3,
    },
    {"input": {"dividend": 7, "divisor": -3}, "expected": -2},
    {"input": {"dividend": 0, "divisor": 1}, "expected": 0},
    {"input": {"dividend": 1, "divisor": 1}, "expected": 1},
    {"input": {"dividend": -1, "divisor": -1}, "expected": 1},
]


def test_solution():
    for test_case in test_cases:
        input = test_case["input"]
        assert test_case["expected"] == Solution().divide(
            input["dividend"], input["divisor"]
        )
