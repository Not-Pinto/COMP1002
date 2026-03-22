from DSALinkedList import DSALinkedList

mylist = DSALinkedList()
exit = False 

print("\nInteracive Menu for DSALinkedList\n")

while exit == False:
    print("\nWould you like to add(1) or remove an item(2), view the list(3), or exit(4)")
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

    elif selection1 == 1 or selection1 == 2:
        selection2 = None
        while selection2 == None:
            try: 
                print("\nWould you like to add/remove from the start(1) or end(2) of the list")
                selection2 = int(input("Please enter 1 or 2: "))
                if 1 > selection2 or selection2 > 2:
                    print("\nOut of range")
                    selection2 = None
            except ValueError: 
                print("\nIntigers only")

        if selection1 == 1:
            value = input("\nplease provide a value to be added to the list: ")
            if selection2 == 1: 
                mylist.insert_first(value)
            else:
                mylist.insert_last(value)
        if selection1 == 2:
            if selection2 == 1:
                try:
                    mylist.remove_first()
                except RuntimeError:
                    print("\nThe list was empty, nothing to remove")
            else:
                try:
                    mylist.remove_last()
                except RuntimeError:
                    print("\nThe list is empty, nothing to remove")
    else:  
        if mylist.is_empty():
            print("\nThe list is currently empty")
        else:
            print()
            for i in range(mylist.list_length() - 1):
                print(mylist.peek_first(), end=", ")
                mylist.insert_last(mylist.remove_first())
            print(mylist.peek_first())
            mylist.insert_last(mylist.remove_first())

