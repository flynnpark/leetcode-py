from typing import List, TypedDict

from solutions.solution_0024 import ListNode, Solution


class CaseDict(TypedDict):
    head: List[int]
    expected: List[int]


test_cases: List[CaseDict] = [
    {
        "input": [1, 2, 3, 4],
        "expected": [2, 1, 4, 3],
    },
    {"input": [], "expected": []},
    {"input": [1], "expected": [1]},
]


def test_solution():
    for test_case in test_cases:
        head = ListNode.from_list(test_case["input"])
        expected = test_case["expected"]
        actual = Solution().swapPairs(head)
        actual = ListNode.to_list(actual)
        assert actual == expected
