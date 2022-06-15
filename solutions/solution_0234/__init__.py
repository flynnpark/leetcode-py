from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        reverse = None

        while fast and fast.next:
            fast = fast.next.next
            reverse, reverse.next, slow = slow, reverse, slow.next

        if fast:
            slow = slow.next

        while reverse and reverse.val == slow.val:
            reverse, slow = reverse.next, slow.next

        return not reverse
