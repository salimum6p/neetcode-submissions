class MyQueue:

    def __init__(self):
        self.stack = []
        self.Queue = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.Queue:
            while self.stack:
                self.Queue.append(self.stack.pop())

        return self.Queue.pop()

    def peek(self) -> int:
        if not self.Queue:
            while self.stack:
                self.Queue.append(self.stack.pop())

        return self.Queue[-1]

    def empty(self) -> bool:
        return not self.stack and not self.Queue