# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(l: list[int]) -> Optional['ListNode']:
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
    def to_list(head: Optional['ListNode']) -> list[int]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return l


class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if not head:
            return None

        if left == right:
            return head

        new_head = start = ListNode(0)
        new_head.next = head

        for _ in range(left - 1):
            if not start.next:
                return head
            start = start.next
        end = start.next

        for _ in range(right - left):
            if not end or not end.next:
                return head
            temp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = temp

        return new_head.next
