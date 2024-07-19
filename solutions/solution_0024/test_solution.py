from typing import TypedDict

from . import ListNode, Solution


class CaseDict(TypedDict):
    input: list[int]
    expected: list[int]


test_cases: list[CaseDict] = [
    {
        'input': [1, 2, 3, 4],
        'expected': [2, 1, 4, 3],
    },
    {'input': [], 'expected': []},
    {'input': [1], 'expected': [1]},
]


def test_solution():
    for test_case in test_cases:
        head = ListNode.from_list(test_case['input'])
        expected = test_case['expected']
        actual = Solution().swapPairs(head)
        actual = ListNode.to_list(actual)
        assert actual == expected
