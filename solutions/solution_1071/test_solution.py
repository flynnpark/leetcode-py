from typing import TypedDict

from . import Solution


class InputDict(TypedDict):
    str1: str
    str2: str


class CaseDict(TypedDict):
    input: InputDict
    expected: str


test_cases: list[CaseDict] = [
    {
        "input": {
            "str1": "ABCABC",
            "str2": "ABC",
        },
        "expected": "ABC",
    },
    {
        "input": {
            "str1": "ABABAB",
            "str2": "ABAB",
        },
        "expected": "AB",
    },
    {
        "input": {
            "str1": "LEET",
            "str2": "CODE",
        },
        "expected": "",
    },
]


def test_solution():
    for test_case in test_cases:
        result = Solution().gcdOfStrings(**test_case["input"])
        assert result == test_case["expected"]
