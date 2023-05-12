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
            "s": "the sky is blue",
        },
        "expected": "blue is sky the",
    },
    {
        "input": {
            "s": "  hello world  ",
        },
        "expected": "world hello",
    },
    {
        "input": {
            "s": "a good   example",
        },
        "expected": "example good a",
    },
]


def test_solution():
    for test_case in test_cases:
        result = Solution().reverseWords(**test_case["input"])
        assert result == test_case["expected"]
