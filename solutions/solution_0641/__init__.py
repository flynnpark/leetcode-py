from typing import Optional


class ListNode:
    def __init__(self, value: int):
        self.value = value
        self.next: Optional[ListNode] = None
        self.prev: Optional[ListNode] = None


class MyCircularDeque:
    def __init__(self, k: int):
        self.head = self.tail = ListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0
        self.k = k

    def addNode(self, value: int, preNode: ListNode):
        node = ListNode(value)
        node.prev = preNode
        node.next = preNode.next
        preNode.next.prev = node
        preNode.next = node
        self.count += 1

    def removeNode(self, preNode: ListNode):
        preNode.prev.next = preNode.next
        preNode.next.prev = preNode.prev
        self.count -= 1

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.addNode(value, self.head)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.addNode(value, self.tail.prev)
        return True

    def deleteFront(self) -> bool:
        if self.count == 0:
            return False

        self.removeNode(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.count == 0:
            return False

        self.removeNode(self.tail.prev.prev)
        return True

    def getFront(self) -> int:
        if self.count == 0:
            return -1

        return self.head.next.value

    def getRear(self) -> int:
        if self.count == 0:
            return -1

        return self.tail.prev.value

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k
