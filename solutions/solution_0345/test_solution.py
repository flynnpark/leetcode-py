from typing import TypedDict

from . import Solution


class InputDict(TypedDict):
    s: str


class CaseDict(TypedDict):
    input: InputDict
    expected: str


test_cases: list[CaseDict] = [
    {
        "input": {
            "s": "hello",
        },
        "expected": "holle",
    },
    {
        "input": {
            "s": "leetcode",
        },
        "expected": "leotcede",
    },
]


def test_solution():
    for test_case in test_cases:
        result = Solution().reverseVowels(**test_case["input"])
        assert result == test_case["expected"]
