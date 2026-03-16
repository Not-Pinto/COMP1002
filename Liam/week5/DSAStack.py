# Adapted from my submission for Practical 3 Stacks and Queues
# can be found on blackborad under the submision link for practical 
# 3 in the DSAStack.py file


from DSALinkedList import DSALinkedList


class DSAStack():

    def __init__(self):
        self.stack = DSALinkedList()
        
    def push(self, value):
        self.stack.insert_last(value)

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Stack is empty")
        return self.stack.remove_last()

    def top(self):
        if self.is_empty():
            raise RuntimeError("Stack is empty")
        return self.stack.peek_last()

    def is_empty(self):
        return self.stack.is_empty()

    def get_count(self):
        return self.stack.list_length()