from DSALinkedList import DSALinkedList
from DSAQueue import DSAQueue
from DSAStack import DSAStack


class DSAGraph():


    def __init__(self):
        self.verticies = DSALinkedList()


    def add_vertex(self, lable, value=None):
        if self.has_vertex(lable):
            raise ValueError
        self.verticies.insert_last(DSAGraphVertex(lable, value))


    def remove_vertex(self, lable):
        vertex = self.get_vertex(lable)
        for i in range(self.verticies.list_length()):
            curr = self.verticies.remove_first()
            if curr != vertex:
                for j in range(curr.links.list_length()):
                    adj = curr.links.peek_first()
                    if adj == lable:
                        curr.links.remove_first()
                    else:
                        curr.links.insert_last(curr.links.remove_first())
                self.verticies.insert_last(curr)


    def add_edge(self, lable1, lable2):
        vertex1 = self.get_vertex(lable1)
        vertex2 = self.get_vertex(lable2)
        duplicate = False
        for i in range(vertex1.links.list_length()):
            if vertex1.links.peek_first() == vertex2:
                duplicate = True
            else:
                vertex1.links.insert_last(vertex1.links.remove_first())
        
        if duplicate == True:
            raise ValueError
        
        if vertex1 == vertex2:
            raise ValueError

        vertex1.add_link(lable2)
        vertex2.add_link(lable1)


    def remove_edge(self,lable1, lable2):
        vertex1 = self.get_vertex(lable1)
        vertex2 = self.get_vertex(lable2)
        removed = False
        for i in range(vertex1.links.list_length()):
            if vertex1.links.peek_first() == lable2:
                vertex1.links.remove_first()
                removed = True
            else:
                vertex1.links.insert_last(vertex1.links.remove_first())
        for i in range(vertex2.links.list_length()):
            if vertex2.links.peek_first() == lable1:
                vertex2.links.remove_first()
            else:
                vertex2.links.insert_last(vertex2.links.remove_first())
        if removed == False:
            raise ValueError


    def has_vertex(self, lable):
        try:
            self.get_vertex(lable)
            return True
        except ValueError:
            return False


    def get_vertex_count(self):
        return self.verticies.list_length()


    def get_edge_count(self):
        edges = 0
        for i in range(self.verticies.list_length()):
            curr = self.verticies.peek_first()
            edges = edges + curr.links.list_length()
            self.verticies.insert_last(self.verticies.remove_first())
        return int(edges / 2)


    def get_vertex(self, label):
        vertex = None
        for i in range(self.verticies.list_length()):
            curr = self.verticies.remove_first()
            self.verticies.insert_last(curr)
            if curr.get_label() == label:
                vertex = curr
        if vertex == None:
            raise ValueError 
        return vertex


    def get_adjacent(self, lable):
        curr = self.get_vertex(lable)
        return curr.get_adjacent()


    def is_adjacent(self, lable1, lable2):
        vertex1 = self.get_vertex(lable1)
        is_adjacent = False
        for i in range(vertex1.links.list_length()):
            curr = vertex1.links.remove_first()
            vertex1.links.insert_last(curr)
            if curr == lable2:
                is_adjacent = True
        return is_adjacent


    def display_as_list(self):
        if self.verticies.is_empty():
            print("Graph is empty")
        else:
            for i in range(self.verticies.list_length()):
                curr = self.verticies.peek_first()
                print(curr.get_label(), end=": ")
                
                if curr.links.is_empty():
                    print()
                else:
                    for j in range(curr.links.list_length() - 1):
                        adj = curr.links.remove_first()
                        print(adj, end=", ")
                        curr.links.insert_last(adj)
                    adj = curr.links.remove_first()
                    print(adj)
                    curr.links.insert_last(adj)
                self.verticies.insert_last(self.verticies.remove_first())
                

    def display_as_matrix(self):
        if self.verticies.is_empty():
            print("Graph is empty")
        else:
            row = DSALinkedList()
            col = DSALinkedList()

            for i in range(self.verticies.list_length()):
                curr = self.verticies.remove_first()
                row.insert_last(curr.get_label())
                col.insert_last(curr.get_label())
                self.verticies.insert_last(curr)

            print("  ", end="")
            for i in range(col.list_length()):
                curr = col.remove_first()
                print(curr, end=" ")
                col.insert_last(curr)
            print()

            for i in range(row.list_length()):
                row_label = row.peek_first()
                print(row_label, end=" ")
                for j in range(col.list_length()):
                    col_label = col.remove_first()
                    if self.is_adjacent(row_label, col_label):
                        print(1, end=" ")
                    else:
                        print(0, end=" ")
                    col.insert_last(col_label)

                print()
                row.insert_last(row.remove_first())


    def clear_visited(self):
        for i in range(self.verticies.list_length()):
            curr = self.verticies.remove_first()
            curr.clear_visited()
            self.verticies.insert_last(curr)


    def breadth_first_search(self):
        T = DSAQueue()
        Q = DSAQueue()

        self.clear_visited()
        if self.verticies.is_empty():
            raise ValueError

        v = self.verticies.peek_first()
        v.set_visited()
        Q.enqueue(v)
        while not Q.is_empty():
            v = Q.dequeue()
            for i in range(v.links.list_length()):
                w = v.links.remove_first()
                v.links.insert_last(w)
                if not w.get_visited():
                    T.enqueue(v)
                    T.enqueue(w)
                    w.set_visited()
                    Q.enqueue(w)
        return T


    def get_next_unvisited(self, vertex):
        next_vertex = None

        for i in range(vertex.links.list_length()):
            curr = vertex.links.remove_first()
            vertex.links.insert_last(curr)

            if not curr.get_visited() and next_vertex is None:
                next_vertex = curr

        return next_vertex


    def depth_first_search(self):
        T = DSAQueue()
        S = DSAStack()
        self.clear_visited()
        if self.verticies.is_empty():
            raise ValueError
        v = self.verticies.peek_first()
        v.set_visited()
        S.push(v)

        while not S.is_empty():
            w = self.get_next_unvisited(v)

            if w is not None:
                T.enqueue(v)
                T.enqueue(w)
                w.set_visited()
                S.push(w)
                v = w
            else:
                v = S.pop()
        return T


    def print_search(self, queue):
        for i in range(queue.get_count() - 1):
            print(queue.peek(), end=", ")
            queue.enqueue(queue.dequeue())
        print(queue.peek())
        queue.enqueue(queue.dequeue())
         


class DSAGraphVertex():

    def __init__(self, label, value):
        self.lable = label
        self.value = value
        self.links = DSALinkedList()
        self.visited = False

    
    def add_link(self, vertex):
        self.links.insert_last(vertex)
        

    def get_label(self):
        return self.lable
    

    def get_value(self):
        return self.value
    

    def get_adjacent(self):
        return self.links


    def set_visited(self):
        self.visited = True

    def clear_visited(self):
        self.visited = False

    def get_visited(self):
        return self.visited