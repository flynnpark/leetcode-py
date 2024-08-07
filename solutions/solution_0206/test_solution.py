from typing import TypedDict

from . import ListNode, Solution


class CaseDict(TypedDict):
    input: list[int]
    expected: list[int]


test_cases: list[CaseDict] = [
    {'input': [1, 2, 3, 4, 5], 'expected': [5, 4, 3, 2, 1]},
    {'input': [1, 2], 'expected': [2, 1]},
    {'input': [], 'expected': []},
]


def test_solution():
    for test_case in test_cases:
        head = ListNode.from_list(test_case['input'])
        expected = test_case['expected']
        actual = Solution().reverseList(head)
        assert ListNode.to_list(actual) == expected
