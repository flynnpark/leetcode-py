# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(l: List[int]) -> Optional["ListNode"]:
        head = None
        prev = None
        for i in l:
            node = ListNode(i)
            if prev:
                prev.next = node
            else:
                head = node
            prev = node
        return head

    @staticmethod
    def to_list(head: Optional['ListNode']) -> List[int]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return l


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        odd = head
        even_head = even = head.next

        while even and even.next:
            odd.next, even.next = even.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head
        return head
