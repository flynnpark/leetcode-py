from typing import List, TypedDict

from solutions.solution_0053 import Solution


class CastDict(TypedDict):
    input: List[int]
    expected: int


test_cases: List[CastDict] = [
    {"input": [-2, 1, -3, 4, -1, 2, 1, -5, 4], "expected": 6},
    {"input": [1], "expected": 6},
    {"input": [5, 4, -1, 7, 8], "expected": 23},
]


def test_solution():
    for test_case in test_cases:
        actual_result = Solution().maxSubArray(test_case["input"])
        assert actual_result == test_case["expected"]
