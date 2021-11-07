import heapq
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
    def mergeKLists(self, lists: List[ListNode]) -> Optional[ListNode]:
        root = result = ListNode(None)
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
