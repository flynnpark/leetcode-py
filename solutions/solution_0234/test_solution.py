from typing import List, TypedDict

from . import ListNode, Solution


class CaseDict(TypedDict):
    input: List[int]
    expected: bool


test_cases: List[CaseDict] = [
    {"input": [1, 2, 2, 1], "expected": True},
    {"input": [1, 2], "expected": False},
]


def arrayToListNode(numbers: List[int]) -> ListNode | None:
    result = ListNode()
    current = result
    for number in numbers:
        current.next = ListNode(number)
        current = current.next
    return result.next


def test_solution():
    for test_case in test_cases:
        actual_result = Solution().isPalindrome(arrayToListNode(test_case["input"]))
        assert actual_result == test_case["expected"]
