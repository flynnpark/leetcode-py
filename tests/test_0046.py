from typing import TypedDict

from solutions.solution_0046 import Solution

CaseDict = TypedDict("CastDict", {"input": list[int], "expected": list[list[int]]})

test_cases: list[CaseDict] = [
    {
        "input": [1, 2, 3],
        "expected": [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
    },
    {
        "input": [0, 1],
        "expected": [[0, 1], [1, 0]],
    },
    {
        "input": [1],
        "expected": [[1]],
    },
]


def test_solution():
    for test_case in test_cases:
        assert Solution().permute(test_case['input']) == test_case['expected']
