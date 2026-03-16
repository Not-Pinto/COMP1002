from DSALinkedList import DSALinkedList


class DSAQueue():

    def __init__(self):
        self.queue = DSALinkedList()

    def is_empty(self):
        return self.queue.is_empty()

    def get_count(self):
        return self.queue.list_length()
    
    def enqueue(self, value):
        self.queue.insert_last(value)

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("Queue is empty")
        return self.queue.remove_first()

    def peek(self):
        if self.is_empty():
            raise RuntimeError("Queue is empty")
        return self.queue.peek_first()