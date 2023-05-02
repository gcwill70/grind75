from collections import deque


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.size: int = 0
        self.cache: dict = {}
        self.hist = deque()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.hist.remove(key)
            self.hist.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.hist.remove(key)
            self.cache[key] = value
        else:
            self.removeOverflow()
            self.cache[key] = value
            self.size += 1
        self.hist.append(key)

    def removeOverflow(self):
        while self.size >= self.capacity:
            key = self.hist.popleft()
            if key in self.cache:
                self.cache.pop(key)
                self.size -= 1
