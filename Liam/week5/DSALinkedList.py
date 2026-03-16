class DSAListNode():

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next 

    def get_previous(self):
        return self.previous

    def set_next(self, next_node):
        self.next = next_node

    def set_previous(self, previous_node):
        self.previous = previous_node


class DSALinkedList():

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_first(self, value):
        new_node = DSAListNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head.set_previous(new_node)
            self.head = new_node

    def insert_last(self, value):
        new_node = DSAListNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_previous(self.tail)  
            self.tail.set_next(new_node) 
            self.tail = new_node         
            
    def is_empty(self):
        if self.head == None:
            return True
        return False
        
    def peek_first(self):
        if self.is_empty():
            raise RuntimeError ("List is empty")
        return self.head.get_value()
    
    def peek_last(self):
        if self.is_empty():
            raise RuntimeError ("List is empty")
        return self.tail.get_value()
        
    def list_length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def remove_first(self):
        if self.is_empty():
            raise RuntimeError ("List is empty")
        if self.head == self.tail:  
            temp = self.head.get_value()
            self.head = None
            self.tail = None
        else:
            temp = self.head.get_value()
            self.head = self.head.get_next()
            self.head.set_previous(None)
        return temp

    def remove_last(self):
        if self.is_empty():
            raise RuntimeError ("List is empty")
        if self.head == self.tail: 
            temp = self.tail.get_value()
            self.head = None
            self.tail = None
        else:
            temp = self.tail.get_value()
            self.tail = self.tail.get_previous()
            self.tail.set_next(None)
        return temp