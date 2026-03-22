from DSAQueue import DSAQueue

class InvalidValueError (ValueError):
    def __init__(self, key):
        super().__init__("Key " + str(key) + " not found")


class InvalidInputError (ValueError):
    def __init__(self, key):
        super().__init__("Key " + str(key) + " already in use")


class DSATreeNode():
    def __init__ (self, value, key):
        self.key = key 
        self.value = value 
        self.left_child = None
        self.right_child = None


    def get_key(self):
        return self.key
    

    def get_value(self):
        return self.value
    

    def get_left(self):
        return self.left_child
    

    def set_left(self, new_left):
        self.left_child = new_left


    def get_right(self):
        return self.right_child
    

    def set_right(self, new_right):
        self.right_child = new_right
          

class DSABinarySearchTree():
      
    def __init__ (self):
        self.root = None


    def find(self, key):
          return self.find_rec(key, self.root)
    

    def find_rec(self, key, curr):
        value = None
        if curr is None:
            raise InvalidValueError (key)   
        elif key == curr.get_key():
            value = curr.get_value()
        elif key < curr.get_key(): 
            value = self.find_rec(key, curr.get_left())
        else: 
            value = self.find_rec(key, curr.get_right())
        return value


    def insert(self, key, value):
        self.root = self.insert_rec(key, value, self.root)
    

    def insert_rec(self, key, value, curr_node):
        update_node = curr_node
        if curr_node is None:
            update_node = DSATreeNode(value, key)
        elif key == curr_node.get_key():
            raise InvalidInputError (key)
        elif key < curr_node.get_key():
            curr_node.set_left(self.insert_rec(key, value, curr_node.get_left()))
        else:
            curr_node.set_right(self.insert_rec(key, value, curr_node.get_right()))
        return update_node


    def delete(self, key):
        self.root = self.delete_rec(key, self.root)
    
    def delete_rec(self, key, curr_node):
        update_node = curr_node
        if curr_node is not None:
            if key == curr_node.get_key():
                update_node = self.delete_node(curr_node)
            elif key < curr_node.get_key():
                curr_node.set_left(self.delete_rec(key, curr_node.get_left()))
            elif key > curr_node.get_key():
                curr_node.set_right(self.delete_rec(key, curr_node.get_right()))
        else: 
            raise InvalidValueError(key)
        return update_node
    

    def delete_node(self, del_node):
        update_node = None
        if del_node.get_left() is None and del_node.get_right() is None:
            update_node = None
        elif del_node.get_left() is not None and del_node.get_right() is None:
            update_node = del_node.get_left()
        elif del_node.get_left() is None and del_node.get_right() is not None:
            update_node = del_node.get_right()
        else:
            update_node = self.promote_successor(del_node.get_right())
            if update_node != del_node.get_right():
                update_node.set_right(del_node.get_right())
            update_node.set_left(del_node.get_left())
        return update_node


    def promote_successor(self, curr):
        successor = curr
        if curr.get_left() == None:
            successor = curr
        else:
            if curr.get_left() != None:
                successor = self.promote_successor(curr.get_left())
                if successor == curr.get_left():
                     curr.set_left(successor.get_right())
        return successor 
            

    def height(self):
          return self.height_rec(self.root)
    

    def height_rec(self, curr_node):
        if curr_node is None:
            height_so_far = -1
        else: 
            left_height = self.height_rec(curr_node.get_left())
            right_height = self.height_rec(curr_node.get_right())
            if left_height > right_height: 
                height_so_far = left_height + 1
            else:
                height_so_far = right_height + 1
        return height_so_far

    
    def min(self):
        if self.root is None:
            raise ValueError("Tree is empty")
        curr_node = self.root
        while curr_node.get_left() is not None:
            curr_node = curr_node.get_left()
        return curr_node.get_key()
    

    def max(self):
        if self.root is None:
            raise ValueError("Tree is empty")
        curr_node = self.root
        while curr_node.get_right() is not None:
            curr_node = curr_node.get_right()
        return curr_node.get_key()
    

    def in_order(self):
        queue = DSAQueue()
        self.in_order_rec(self.root, queue)
        return queue
    

    def in_order_rec(self, curr, queue):
        if curr is not None:
            self.in_order_rec(curr.get_left(), queue)
            queue.enqueue(curr.get_value())
            self.in_order_rec(curr.get_right(), queue)


    def pre_order(self):  
        queue = DSAQueue() 
        self.pre_order_rec(self.root, queue)
        return queue
    

    def pre_order_rec(self, curr, queue):
        if curr is not None:
            queue.enqueue(curr.get_value())
            self.pre_order_rec(curr.get_left(), queue)
            self.pre_order_rec(curr.get_right(), queue)


    def post_order(self): 
        queue = DSAQueue()
        self.post_order_rec(self.root, queue)
        return queue


    def post_order_rec(self, curr, queue):
        if curr is not None:
            self.post_order_rec(curr.get_left(), queue)
            self.post_order_rec(curr.get_right(), queue)
            queue.enqueue(curr.get_value())     

    
    def is_empty(self):
        if self.root is None:
            return True
        return False