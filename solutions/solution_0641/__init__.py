class ListNode:
    def __init__(self, value: int | None):
        self.value = value
        self.next: ListNode | None = None
        self.prev: ListNode | None = None


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
        if preNode.next:
            preNode.next.prev = node
        preNode.next = node
        self.count += 1

    def removeNode(self, preNode: ListNode):
        if preNode.prev:
            preNode.prev.next = preNode.next
        if preNode.next:
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

        if self.tail.prev:
            self.addNode(value, self.tail.prev)
            return True

        return False

    def deleteFront(self) -> bool:
        if self.count == 0:
            return False

        self.removeNode(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.count == 0:
            return False

        if self.tail.prev:
            self.removeNode(self.tail.prev)
            return True

        return False

    def getFront(self) -> int:
        if self.count == 0:
            return -1

        if self.head.next and self.head.next.value is not None:
            return self.head.next.value

        return -1

    def getRear(self) -> int:
        if self.count == 0:
            return -1

        if self.tail.prev and self.tail.prev.value is not None:
            return self.tail.prev.value

        return -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k
