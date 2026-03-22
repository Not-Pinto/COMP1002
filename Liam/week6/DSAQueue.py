# Adapted from my submission for Practical 3 Stacks and Queues
# can be found on blackborad under the submision link for practical 
# 3 in the DSAQueue.py file

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
    

    def print_queue(self):
        if self.is_empty:
            raise ValueError("Empty Queue")
        for i in range(self.get_count() - 1):
            print(self.dequeue(), end=", ")
        print(self.dequeue())