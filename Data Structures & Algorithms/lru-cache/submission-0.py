class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hmap = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1
        node = self.hmap[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            node = self.hmap[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            if len(self.hmap) == self.capacity:
                lru = self.tail.prev
                lru.prev.next = self.tail
                self.tail.prev = lru.prev
                del self.hmap[lru.key]
            node = Node(key, value)
            self.hmap[key] = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
