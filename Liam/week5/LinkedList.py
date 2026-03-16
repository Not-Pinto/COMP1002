import numpy as np

class DSAlistNode():

    def __init__(self, value):
        self.value = value


class DSALinkedList():

    def __init__(self, value):
        self.next = None
        self.previous = None
        self.head = None
        self.tail = None