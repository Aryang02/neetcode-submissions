class ListNode:
    def __init__(self, key: int = 0, val: Optional[int] = 0, next: Optional[ListNode] = None, prev: Optional[ListNode] = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0
        self.map = {}
        self.last = None

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            if self.size==self.capacity:
                lru = self.head.next
                self.remove(lru)
                del self.map[lru.key]
                self.size -= 1
            new = ListNode(key, value)
            self.add(new)
            self.map[key] = new
            self.size += 1



