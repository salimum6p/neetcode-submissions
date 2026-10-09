
from collections import deque

class MyStack:

    def __init__(self):
        self.stack = deque()
        self.Queue = deque()

    def push(self, x: int) -> None:
        self.Queue.append(x)

        while self.stack:
            self.Queue.append(self.stack.popleft())

        self.stack, self.Queue = self.Queue, self.stack

    def pop(self) -> int:
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return not self.stack
