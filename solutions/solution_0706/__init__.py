import collections


class ListNode:
    def __init__(self, key: int | None = None, value=None):
        self.key: int | None = key
        self.value: int | None = value
        self.next: ListNode | None = None


class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def _get_index(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._get_index(key)
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next

        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = self._get_index(key)
        if self.table[index].value is None:
            return -1
        p = self.table[index]
        while p:
            if p.key == key and p.value is not None:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        index = self._get_index(key)
        if self.table[index].value is None:
            return

        p = self.table[index]
        if p.key == key:
            self.table[index] = p.next if p.next else ListNode()
            return

        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
