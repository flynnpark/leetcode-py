from typing import TypedDict

from . import ListNode, Solution


class CaseDict(TypedDict):
    input: list[int]
    expected: list[int]


test_cases: list[CaseDict] = [
    {
        'input': [1, 2, 3, 4, 5],
        'expected': [1, 3, 5, 2, 4],
    },
    {'input': [2, 1, 3, 5, 6, 4, 7], 'expected': [2, 3, 6, 7, 1, 5, 4]},
]


def test_solution():
    for test_case in test_cases:
        head = ListNode.from_list(test_case['input'])
        expected = test_case['expected']
        actual = Solution().oddEvenList(head)
        actual = ListNode.to_list(actual)
        assert actual == expected
