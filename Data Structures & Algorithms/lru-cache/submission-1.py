
from collections import deque


class Cache:
    def __init__(self):
        self.order = deque()  # keys: LRU on the left, MRU on the right

    def use(self, key):
        self.order.remove(key)
        self.order.append(key)

    def insert(self, key):
        self.order.append(key)

    def remove_lru(self):
        return self.order.popleft()


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} 
        self.order = Cache()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.order.use(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.order.use(key)
            self.cache[key] = value
            return

        self.cache[key] = value
        self.order.insert(key)

        if len(self.cache) > self.cap:
            lru = self.order.remove_lru()
            del self.cache[lru]
