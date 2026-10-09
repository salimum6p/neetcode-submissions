class MyQueue:

    def __init__(self):
        self.stack = []
        self.Queue = []
        

    def push(self, x: int) -> None:

        while self.Queue:
            self.stack.append(self.Queue.pop())
        self.Queue.append(x)
        while self.stack:
            self.Queue.append(self.stack.pop())
        

    def pop(self) -> int:
        return self.Queue.pop() if self.Queue else  0

    def peek(self) -> int:
        return self.Queue[-1] if self.Queue else  0
        

    def empty(self) -> bool:
        return False if self.Queue else True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()