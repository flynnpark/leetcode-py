from typing import TypedDict

from . import Solution


class InputDict(TypedDict):
    word1: str
    word2: str


class CaseDict(TypedDict):
    input: InputDict
    expected: str


test_cases: list[CaseDict] = [
    {
        "input": {
            "word1": "abc",
            "word2": "pqr",
        },
        "expected": "apbqcr",
    },
    {
        "input": {
            "word1": "ab",
            "word2": "pqrs",
        },
        "expected": "apbqrs",
    },
    {
        "input": {
            "word1": "abcd",
            "word2": "pq",
        },
        "expected": "apbqcd",
    },
]


def test_solution():
    for test_case in test_cases:
        result = Solution().mergeAlternately(**test_case["input"])
        assert result == test_case["expected"]
