import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val: Optional[int] = None, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(l: List[int]) -> "ListNode":
        head = ListNode(None)
        prev = ListNode(None)
        for i in l:
            node = ListNode(i)
            if prev.val is not None:
                prev.next = node
            else:
                head = node
            prev = node
        return head

    @staticmethod
    def to_list(head: Optional["ListNode"]) -> List[int]:
        l = []
        while head:
            if head.val is not None:
                l.append(head.val)
            head = head.next
        return l


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> Optional[ListNode]:
        root = result = ListNode(0)
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            node = heapq.heappop(heap)
            index = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, index, result.next))

        return root.next
