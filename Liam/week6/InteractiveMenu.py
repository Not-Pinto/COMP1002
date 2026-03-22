from DSAQueue import DSAQueue
from DSATree import DSABinarySearchTree, InvalidValueError, InvalidInputError

mytree = DSABinarySearchTree()
exit = False 

print("\n\nInteracive Menu for DSATree")

while exit == False:
    print("\nWould you like to add(1) or delete a node (2), display the tree(3), or exit(4)")
    selection1 = None
    while selection1 == None:
        try: 
            selection1 = int(input("Please enter 1, 2, 3, or 4: "))
            if 1 > selection1 or selection1 > 4:
                print("\nOut of range")
                selection1 = None
        except ValueError: 
            print("\nIntegers only")
        
    if selection1 == (4):
        exit = True

    elif selection1 == 1:
        key = None
        while key == None:
            try: 
                print("\nEnter the key of the node you would like to add")
                key = int(input("Please enter a positive int: "))
                if 1 > key:
                    print("\nOut of range (positive only)")
                    key = None
            except ValueError: 
                print("\nIntigers only")
        print("\nEnter the value of the node you would like to add")
        value = input()
        try:
            mytree.insert(key, value)
        except InvalidInputError:
            print("The key", key, "is already in use, failed to add node")


    elif selection1 == 2:
        if mytree.is_empty():
            print("\nThe tree is empty (no nodes to delete)")
        else:
            try: 
                print("\nEnter the key of the node you would like to delete")
                key = int(input("Please enter a positive int: "))
                if 1 > key:
                    print("\nOut of range (positive only)")
                    key = None
                else:
                    try:
                        mytree.delete(key)
                    except InvalidValueError:
                        print("\nThere is no node with this key")
            except ValueError: 
                print("\nIntigers only")
                print("\nEnter the value of the node you would like to delete")

            
    else:
        if mytree.is_empty():
            print("\nThe tree is currently empty")
        else:
            print("\nWould you like to display the tree in-order(1), pre-order(2) post-order(3)")
            selection2 = None
            while selection2 == None:
                try: 
                    selection2 = int(input("Please enter 1, 2 or 3: "))
                    if 1 > selection2 or selection2 > 3:
                        print("\nOut of range")
                        selection2 = None
                except ValueError: 
                    print("\nIntegers only")

            if selection2 == 1:
                display = mytree.in_order()
            elif selection2 == 2:
                display = mytree.pre_order()
            elif selection2 == 3:
                display = mytree.post_order()

            print("\nTree:")
            for i in range(display.get_count() - 1):
                print(display.dequeue(), end=", ")
            print(display.dequeue())
