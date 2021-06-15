from typing import List, TypedDict
from solutions.solution_0021 import ListNode, Solution,

class CaseInput(TypedDict):
    l1: ListNode
    l2: ListNode


class CaseDict(TypedDict):
    input: CaseInput
    expected: str


test_cases: List[CaseDict] = [
    {"input": { 'l1': [1, 2, 4], 'l2': [1, 3, 4]  }, "expected": [1,1,2,3,4,4]},
    {"input": { 'l1': [], 'l2':  [] }, "expected": []},
    {"input": { 'l1': [], 'l2':[0]   }, "expected": [0]},
]


def test_solution():
    for test_case in test_cases:
        actual_result = Solution().mergeTwoLists(**test_case["input"])
        assert actual_result == test_case["expected"]
