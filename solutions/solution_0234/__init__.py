from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = fast = head
        reverse = None

        while fast and fast.next and slow:
            fast = fast.next.next
            reverse, reverse.next, slow = slow, reverse, slow.next

        if fast and slow:
            slow = slow.next

        while reverse and slow and reverse.val == slow.val:
            reverse, slow = reverse.next, slow.next

        return not reverse
