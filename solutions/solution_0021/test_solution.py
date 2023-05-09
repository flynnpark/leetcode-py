from typing import Optional, TypedDict

from . import ListNode, Solution

CaseInput = TypedDict("CaseInput", {"l1": list[int], "l2": list[int]})
CaseDict = TypedDict("CaseDict", {"input": CaseInput, "expected": list[int]})


test_cases: list[CaseDict] = [
    {"input": {"l1": [1, 2, 4], "l2": [1, 3, 4]}, "expected": [1, 1, 2, 3, 4, 4]},
    {"input": {"l1": [], "l2": []}, "expected": []},
    {"input": {"l1": [], "l2": [0]}, "expected": [0]},
]


def arrayToListNode(numbers: list[int]) -> Optional[ListNode]:
    result = ListNode()
    current = result
    for number in numbers:
        current.next = ListNode(number)
        current = current.next
    return result.next


def test_solution():
    for test_case in test_cases:
        actual_result = Solution().mergeTwoLists(
            l1=arrayToListNode(test_case["input"]["l1"]),
            l2=arrayToListNode(test_case["input"]["l2"]),
        )
        assert actual_result == arrayToListNode(test_case["expected"])

    for test_case in test_cases:
        actual_result = Solution().mergeTwoListsRecursive(
            l1=arrayToListNode(test_case["input"]["l1"]),
            l2=arrayToListNode(test_case["input"]["l2"]),
        )
        assert actual_result == arrayToListNode(test_case["expected"])
