from typing import List
from solutions.solution_0002 import ListNode, Solution


def arrayToListNode(numbers: List[int]) -> ListNode:
    result = ListNode()
    current = result
    for number in numbers:
        current.next = ListNode(number)
        current = current.next
    return result.next


def test_solution():
    assert Solution().addTwoNumbers(
        l1=arrayToListNode([2, 4, 3]), l2=arrayToListNode([5, 6, 4])
    ) == arrayToListNode([7, 0, 8])
    assert Solution().addTwoNumbers(
        l1=arrayToListNode([0]), l2=arrayToListNode([0])
    ) == arrayToListNode([0])
    assert Solution().addTwoNumbers(
        l1=arrayToListNode([9, 9, 9, 9, 9, 9, 9]), l2=arrayToListNode([9, 9, 9, 9])
    ) == arrayToListNode(
        [
            8,
            9,
            9,
            9,
            0,
            0,
            0,
            1,
        ]
    )
