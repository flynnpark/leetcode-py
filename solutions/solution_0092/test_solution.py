from typing import TypedDict

from . import ListNode, Solution


class InputDict(TypedDict):
    head: list[int]
    left: int
    right: int


class CaseDict(TypedDict):
    input: InputDict
    expected: list[int]


test_cases: list[CaseDict] = [
    {
        'input': {'head': [1, 2, 3, 4, 5], 'left': 2, 'right': 4},
        'expected': [1, 4, 3, 2, 5],
    },
    {'input': {'head': [5], 'left': 1, 'right': 1}, 'expected': [5]},
]


def test_solution():
    for test_case in test_cases:
        head = ListNode.from_list(test_case['input']['head'])
        expected = test_case['expected']
        actual = Solution().reverseBetween(
            head=head,
            left=test_case['input']['left'],
            right=test_case['input']['right'],
        )
        actual = ListNode.to_list(actual)
        assert actual == expected
