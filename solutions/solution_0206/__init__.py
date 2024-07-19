from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
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
            if head.val is not None:
                l.append(head.val)
            head = head.next
        return l


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev
