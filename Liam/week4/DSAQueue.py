import numpy as np
class DSAQueue():

    def __init__(self, size=10):
        self.size = size 
        self.count = 0
        self.queue = np.empty(size, dtype=object)

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
    


class shuffle_queue(DSAQueue):
    
    def __init__(self, size=10):
        super().__init__(size)
    
    def enqueue(self, value):
        if self.is_full():
            raise RuntimeError("Queue is full")
        self.queue[self.count] = value
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("Queue is empty")
        value = self.queue[0]
        for i in range(0, self.count - 1):
            self.queue[i] = self.queue[i + 1]
        self.count -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise RuntimeError("Queue is empty")
        return self.queue[0]



class circular_queue(DSAQueue):
    def __init__(self, size=10):
        super().__init__(size)
        self.head = 0
        self.tail = 0

    def enqueue(self, value):
        if self.is_full():
            raise RuntimeError("Queue is full")
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("Queue is empty")
        value = self.queue[self.head]
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise RuntimeError("Queue is empty")
        return self.queue[self.head]