from typing import Optional


class ListNode:
    def __init__(self, val: int | None = None, next: Optional['ListNode'] = None):
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
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head
