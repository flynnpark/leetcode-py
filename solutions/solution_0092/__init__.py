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
    def to_list(head: "ListNode") -> List[int]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return l


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        pass
