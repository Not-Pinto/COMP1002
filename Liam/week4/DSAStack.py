import numpy as np

class DSAStack():
    def __init__(self, size=10):
        self.size = size
        self.count = 0
        self.stack = np.empty(size, dtype=object)
        
    def push(self, value):
        if self.is_full():
            raise RuntimeError("Stack is full")
        self.stack[self.count] = value
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Stack is empty")
        value = self.stack[self.count - 1]
        self.count -= 1
        return value

    def top(self):
        if self.is_empty():
            raise RuntimeError("Stack is empty")
        return self.stack[self.count-1]

    def is_empty(self):
        if self.count == 0:
            return True
        return False

    def is_full(self):
        if self.count == self.size:
            return True 
        return False

    def get_count(self):
        return self.count