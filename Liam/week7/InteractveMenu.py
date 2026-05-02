from DSAGraphs import DSAGraph

mygraph = DSAGraph()

mygraph.add_vertex("A")
mygraph.add_vertex("B")
mygraph.add_vertex("C")
mygraph.add_vertex("D")
mygraph.add_vertex("E")
mygraph.add_vertex("F")
mygraph.add_vertex("G")
mygraph.add_edge("A", "B")
mygraph.add_edge("A", "D")
mygraph.add_edge("A", "C")
mygraph.add_edge("D", "C")
mygraph.add_edge("D", "F")
mygraph.add_edge("B", "E")
mygraph.add_edge("E", "F")
mygraph.add_edge("E", "G")
mygraph.add_edge("F", "G")

exit = False
print("\n\nInteractive Menu for DSAGraph")
while exit == False:
    print("\nWould you like to edit nodes(1), edit edges(2), display graph(3), search graph(4), or exit(5)")
    selection1 = None
    while selection1 == None:
        try:
            selection1 = int(input("Please enter 1, 2, 3, 4, or 5: "))
            if 1 > selection1 or selection1 > 5:
                print("\nOut of range")
                selection1 = None
        except ValueError:
            print("\nIntegers only") 

    if selection1 == 5:
        exit = True

    elif selection1 == 1:
        print("\nWould you like to add a node(1) or delete a node(2)")
        selection2 = None

        while selection2 == None:
            try:
                selection2 = int(input("Please enter 1 or 2: "))
                if 1 > selection2 or selection2 > 2:
                    print("\nOut of range")
                    selection2 = None
            except ValueError:
                print("\nIntegers only")

        if selection2 == 1:
            print("\nEnter the label of the node you would like to add")
            label = input("Please enter a label: ")
            try:
                mygraph.add_vertex(label)
            except ValueError:
                print("The label", label, "is already in use, failed to add node")

        elif selection2 == 2:
            if mygraph.verticies.is_empty():
                print("\nThe graph is empty (no nodes to delete)")
            else:
                print("\nEnter the label of the node you would like to delete")
                label = input("Please enter a label: ")
                try:
                    mygraph.remove_vertex(label)
                except ValueError:
                    print("\nThere is no node with this label")

    elif selection1 == 2:
        print("\nWould you like to add an edge(1) or delete an edge(2)")
        selection2 = None

        while selection2 == None:
            try:
                selection2 = int(input("Please enter 1 or 2: "))
                if 1 > selection2 or selection2 > 2:
                    print("\nOut of range")
                    selection2 = None
            except ValueError:
                print("\nIntegers only")

        if selection2 == 1:
            print("\nEnter the first node label")
            label1 = input("Please enter a label: ")
            if not mygraph.has_vertex(label1):
                print("\nThe first vertex does not exist")
            else:
                print("\nEnter the second node label")
                label2 = input("Please enter a label: ")
                if not mygraph.has_vertex(label2):
                    print("\nThe second vertex does not exist")
                else:
                    try:
                        mygraph.add_edge(label1, label2)
                    except ValueError:
                        print("\nFailed to add edge")

        elif selection2 == 2:
            if mygraph.verticies.is_empty():
                print("\nThe graph is empty (no edges to delete)")
            else:
                print("\nEnter the first node label")
                label1 = input("Please enter a label: ")
                print("\nEnter the second node label")
                label2 = input("Please enter a label: ")
                try:
                    mygraph.remove_edge(label1, label2)
                except ValueError:
                    print("\nThere is no edge between these nodes")

    elif selection1 == 3:
        if mygraph.verticies.is_empty():
            print("\nThe graph is currently empty")
        else:
            print("\nWould you like to display as list(1) or matrix(2)")
            selection2 = None

            while selection2 == None:
                try:
                    selection2 = int(input("Please enter 1 or 2: "))
                    if 1 > selection2 or selection2 > 2:
                        print("\nOut of range")
                        selection2 = None
                except ValueError:
                    print("\nIntegers only")

            if selection2 == 1:
                print("\nGraph as list:")
                mygraph.display_as_list()
            elif selection2 == 2:
                print("\nGraph as matrix:")
                mygraph.display_as_matrix()

    elif selection1 == 4:
        if mygraph.verticies.is_empty():
            print("\nThe graph is currently empty")
        else:
            print("\nWould you like to do breadth first search(1) or depth first search(2)")
            selection2 = None

            while selection2 == None:
                try:
                    selection2 = int(input("Please enter 1 or 2: "))
                    if 1 > selection2 or selection2 > 2:
                        print("\nOut of range")
                        selection2 = None
                except ValueError:
                    print("\nIntegers only")

            if selection2 == 1:
                print("\nBreadth First Search:")
                try:
                    mygraph.print_search(mygraph.breadth_first_search())
                except ValueError:
                    print("The graph is empty")

            elif selection2 == 2:
                print("\nDepth First Search:")
                try:
                    mygraph.print_search(mygraph.depth_first_search())
                except ValueError:
                    print("The graph is empty")