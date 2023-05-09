from typing import TypedDict

from . import Solution

CaseDict = TypedDict("CaseDict", {"input": list[list[str]], "expected": int})

test_cases: list[CaseDict] = [
    {
        "input": [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ],
        "expected": 1,
    },
    {
        "input": [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ],
        "expected": 3,
    },
]


def test_solution():
    for test_case in test_cases:
        assert Solution().numIslands(test_case["input"]) == test_case["expected"]
