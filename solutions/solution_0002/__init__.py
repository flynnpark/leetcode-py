# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
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
    def addTwoNumbers(
        self,
        l1: ListNode | None,
        l2: ListNode | None,
    ) -> ListNode | None:
        result = ListNode(0)
        current = result
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry

            carry = sum // 10
            rest = sum % 10

            current.next = ListNode(rest)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            current.next = ListNode(carry)

        return result.next
