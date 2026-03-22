from DSATree import DSABinarySearchTree, InvalidInputError, InvalidValueError
from DSAQueue import DSAQueue



def tree_test():
    print("\nTest for DSATree\n")
    tree = DSABinarySearchTree()

    print("Checking is_empty method, expected True:", tree.is_empty())

    print("\nAdding node: key 50 and value A")
    tree.insert(50, "A")
    print("Adding node: key 30 and value B")
    tree.insert(30, "B")
    print("Adding node: key 70 and value C")
    tree.insert(70, "C")
    print("Adding node: key 20 and value D")
    tree.insert(20, "D")
    print("Adding node: key 40 and value E")
    tree.insert(40, "E")
    print("Adding node: key 60 and value F")
    tree.insert(60, "F")
    print("Adding node: key 80 and value G")
    tree.insert(80, "G")

    print("Checking is_empty and insert method, expected False:", tree.is_empty())

    print("Checking find method")

    print("Finding key 50, expected A:", tree.find(50))
    print("Finding key 20, expected D:", tree.find(20))
    print("Finding key 80, expected G:", tree.find(80))

    print("Checking min method, expected 20:", tree.min())
    print("Checking max method, expected 80:", tree.max())
    print("Checking height method, expected 2:", tree.height())
    print("Checking balance method:", tree.balance())

    print("\nChecking in_order, expected D, B, E, A, F, C, G")
    display = tree.in_order()
    display.print_queue()

    print("\nChecking pre_order, expected A, B, D, E, C, F, G")
    display = tree.pre_order()
    display.print_queue()

    print("\nChecking post_order, expected D, E, B, F, G, C, A")
    display = tree.post_order()
    display.print_queue()

    print("\nChecking delete method (no children)")
    print("Deleting key 20 (D)")
    tree.delete(20)
    print("Checking in_order and confirming delete, expected B, E, A, F, C, G")
    display = tree.in_order()
    display.print_queue()

    print("\nChecking delete method (one child)")
    print("Deleting key 30 (B)")
    tree.delete(30)
    print("Checking in_order and delete, expected E, A, F, C, G")
    display = tree.in_order()
    display.print_queue()

    print("\nDeleting key 50 (A) (two children)")
    tree.delete(50)
    print("Checking in_order and delete, expected: E, F, C, G")
    display = tree.in_order()
    display.print_queue()

    print("\nChecking error handling")

    print("Attempting to find key that does not exist")
    print("Should receive InvalidValueError")
    try:
        tree.find(1)
    except InvalidValueError:
        print("Error recived corectly")

    print("Attempting to create a node with a key already in use")
    print("Should receive InvalidInputError")
    try:
        tree.insert(70, "C")
    except InvalidInputError:
        print("Error recived corectly")

    print("Attempting to delete key that does not exist")
    print("Should receive InvalidValueError")
    try:
        tree.delete(1)
    except InvalidValueError:
        print("Error recived corectly")

    print("End of tree test")


tree_test()