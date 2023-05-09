from typing import List, TypedDict

from . import Solution


class CastDict(TypedDict):
    input: str
    expected: int


test_cases: List[CastDict] = [
    {"input": "Hello World", "expected": 5},
    {"input": " ", "expected": 0},
]


def test_solution():
    for test_case in test_cases:
        actual_result = Solution().lengthOfLastWord(test_case["input"])
        assert actual_result == test_case["expected"]
