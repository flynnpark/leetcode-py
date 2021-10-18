from typing import List, TypedDict

from solutions.solution_0092 import ListNode, Solution


class CaseDict(TypedDict):
    head: List[int]
    expected: List[int]


test_cases: List[CaseDict] = [
    {
        "input": {"head": [1, 2, 3, 4, 5], "left": 2, "right": 4},
        "expected": [1, 4, 3, 2, 5],
    },
    {"input": {"head": [5], "left": 1, "right": 1}, "expected": [5]},
]


def test_solution():
    for test_case in test_cases:
        head = ListNode.from_list(test_case["input"])
        expected = test_case["expected"]
        actual = Solution().reverseBetween(head)
        actual = ListNode.to_list(actual)
        assert actual == expected
