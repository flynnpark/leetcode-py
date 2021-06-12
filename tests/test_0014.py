from typing import List
from typing_extensions import TypedDict
from solutions.solution_0014 import Solution


class CaseDict(TypedDict):
    input: List[str]
    expected: str


test_cases: List[CaseDict] = [
    {"input": ["flower", "flow", "flight"], "expected": "fl"},
    {"input": ["dog", "racecar", "car"], "expected": ""},
]


def test_solution():
    for test_case in test_cases:
        actual_result = Solution().longestCommonPrefix(test_case["input"])
        assert actual_result == test_case["expected"]
