import math
class MinStack:

    def __init__(self):
        self._data = []
        self._min_stack = []
    def push(self, val: int) -> None:
        self._data.append(val)
        try: 
            if self._min_stack[-1] >= val:
                self._min_stack.append(val)
        except IndexError:
            self._min_stack.append(val)

    def pop(self) -> None:
        if not self._data:
            raise IndexError("empty stack")
        val = self._data.pop()
        try:
            if self._min_stack[-1] == val:
                self._min_stack.pop()
        except IndexError:
            pass
        return val
    def top(self) -> int:
        if not self._data:
            raise IndexError("empty stack")
        return self._data[-1]       

    def getMin(self) -> int:
        try:
            return self._min_stack[-1]
        except IndexError:
            return None
        
