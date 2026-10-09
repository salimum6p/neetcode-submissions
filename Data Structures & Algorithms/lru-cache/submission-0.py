
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get_lru(self):
        return self.left.next


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  
        self.dll = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.dll.remove(node)
        self.dll.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.dll.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.dll.insert(node)

        if len(self.cache) > self.cap:
            lru = self.dll.get_lru()
            self.dll.remove(lru)
            del self.cache[lru.key]
