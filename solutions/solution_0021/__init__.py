# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val: int | None = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        while self and other and self.val == other.val:
            self = self.next
            other = other.next
        if not self and not other:
            return True
        return False


class Solution:
    def mergeTwoLists(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        result = ListNode(None)
        current = result

        while l1 and l2 and l1.val and l2.val:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        if not l1:
            current.next = l2
        if not l2:
            current.next = l1

        return result.next

    def mergeTwoListsRecursive(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val and l2.val and l1.val < l2.val:
            l1.next = self.mergeTwoListsRecursive(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoListsRecursive(l1, l2.next)
            return l2
