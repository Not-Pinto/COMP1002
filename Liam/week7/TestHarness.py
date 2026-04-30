from DSAGraphs import DSAGraph

def graph_test():
    print("\nTest for DSAGraph\n")
    graph = DSAGraph()

    print("Checking get_vertex_count on empty graph, expected 0:", graph.get_vertex_count())
    print("Checking get_edge_count on empty graph, expected 0:", graph.get_edge_count())

    print("\nAdding vertices A, B, C, D, E")
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")

    print("Checking has_vertex method")
    print("Has vertex A, expected True:", graph.has_vertex("A"))
    print("Has vertex C, expected True:", graph.has_vertex("C"))
    print("Has vertex Z, expected False:", graph.has_vertex("Z"))

    print("\nChecking get_vertex_count, expected 5:", graph.get_vertex_count())

    print("\nAdding edges A-B, A-C, B-D, C-D, D-E")
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "D")
    graph.add_edge("D", "E")

    print("Checking get_edge_count, expected 5:", graph.get_edge_count())

    print("\nChecking is_adjacent method")
    print("A adjacent to B, expected True:", graph.is_adjacent("A", "B"))
    print("A adjacent to C, expected True:", graph.is_adjacent("A", "C"))
    print("B adjacent to C, expected False:", graph.is_adjacent("B", "C"))
    print("D adjacent to E, expected True:", graph.is_adjacent("D", "E"))
    print("A adjacent to E, expected False:", graph.is_adjacent("A", "E"))

    print("\nChecking get_adjacent method")
    print("Adjacent to A, expected B, C")
    adj = graph.get_adjacent("A")
    for i in range(adj.list_length() - 1):
        print(adj.peek_first(), end=", ")
        adj.insert_last(adj.remove_first())
    print(adj.peek_first())
    adj.insert_last(adj.remove_first())

    print("Adjacent to D, expected B, C, E")
    adj = graph.get_adjacent("D")
    for i in range(adj.list_length() - 1):
        print(adj.peek_first(), end=", ")
        adj.insert_last(adj.remove_first())
    print(adj.peek_first())
    adj.insert_last(adj.remove_first())    

    print("\nChecking display_as_list")
    graph.display_as_list()

    print("\nChecking display_as_matrix")
    graph.display_as_matrix()

    print("Checking DFS")
    graph.print_search(graph.depth_first_search())

    print("Checking BFS")
    graph.print_search(graph.breadth_first_search())

    print("\nChecking remove_edge method")
    print("Removing edge A-C")
    graph.remove_edge("A", "C")
    print("Checking A adjacent to C, expected False:", graph.is_adjacent("A", "C"))
    print("Checking get_edge_count, expected 4:", graph.get_edge_count())

    print("\nChecking display_as_list after removing edge A-C")
    graph.display_as_list()

    print("\nChecking remove_vertex method")
    print("Removing vertex D")
    graph.remove_vertex("D")
    print("Checking has_vertex D, expected False:", graph.has_vertex("D"))
    print("Checking get_vertex_count, expected 4:", graph.get_vertex_count())

    print("Checking adjacencies involving removed vertex")
    print("B adjacent to D should now error or be False depending on your implementation")
    try:
        print(graph.is_adjacent("B", "D"))
    except ValueError:
        print("Error received correctly")

    print("Checking get_edge_count after removing D")
    print("Expected 1 if only A-B remains and E becomes isolated:", graph.get_edge_count())

    print("\nChecking display_as_list after removing vertex D")
    graph.display_as_list()

    print("\nChecking display_as_matrix after removing vertex D")
    graph.display_as_matrix()

    print("\nChecking error handling")

    print("Attempting to add duplicate vertex A")
    print("Should receive ValueError")
    try:
        graph.add_vertex("A")
    except ValueError:
        print("Error received correctly")

    print("Attempting to add edge with non-existent vertex")
    print("Should receive ValueError")
    try:
        graph.add_edge("A", "Z")
    except ValueError:
        print("Error received correctly")

    print("Attempting to remove edge that does not exist")
    print("Should receive ValueError")
    try:
        graph.remove_edge("A", "E")
    except ValueError:
        print("Error received correctly")

    print("Attempting to remove vertex that does not exist")
    print("Should receive ValueError")
    try:
        graph.remove_vertex("Z")
    except ValueError:
        print("Error received correctly")

    print("Attempting to add self-loop A-A")
    print("Should receive ValueError")
    try:
        graph.add_edge("A", "A")
    except ValueError:
        print("Error received correctly")

    print("\nEnd of graph test")


graph_test()