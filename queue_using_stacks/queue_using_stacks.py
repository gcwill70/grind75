from collections import deque


class MyQueue:
    def __init__(self):
        self.first = deque()
        self.second = deque()

    def push(self, x: int) -> None:
        self.first.append(x)

    def pop(self) -> int:
        # pop all elements from first to second
        self.__pop_all(self.first, self.second)
        # get top element from second
        val = self.second.pop()
        # push all elements back onto first
        self.__pop_all(self.second, self.first)
        return val

    def __pop_all(self, one: deque, two: deque):
        while len(one) > 0:
            two.append(one.pop())

    def peek(self) -> int:
        # pop all elements from first to second
        self.__pop_all(self.first, self.second)
        val = self.second[-1]
        # push all elements back onto first
        self.__pop_all(self.second, self.first)
        return val

    def empty(self) -> bool:
        return len(self.first) == 0
