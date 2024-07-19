from typing import TypedDict

from . import ListNode, Solution


class CaseDict(TypedDict):
    input: list[list[int]]
    expected: list[int]


test_cases: list[CaseDict] = [
    {'input': [[1, 4, 5], [1, 3, 4], [2, 6]], 'expected': [1, 1, 2, 3, 4, 4, 5, 6]},
    {'input': [], 'expected': []},
    {'input': [[]], 'expected': []},
]


def test_solution():
    for test_case in test_cases:
        input = [ListNode.from_list(l) for l in test_case['input']]
        expected = test_case['expected']
        actual = Solution().mergeKLists(input)
        assert ListNode.to_list(actual) == expected
