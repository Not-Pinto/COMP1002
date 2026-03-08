facOrFib = None
while facOrFib is None:
    try: 
        print("Would you like to see Factorial(1) or Fibonnaci(2)?")
        facOrFib = int(input("Please eneter an int: "))
    except ValueError as err:
        print("Please only enter an int, 1 or 2, Error:", err)
    else:
        if 1 > facOrFib or 2 < facOrFib:
            print("Please only enter an int, 1 or 2, Error: OutOfRange")
            facOrFib = None

IteOrRec = None
while IteOrRec is None:
    try: 
        print("Would you like to see Iterative(1) or Recursive(2)?")
        IteOrRec = int(input("Please eneter an int: "))
    except ValueError as err:
        print("Please only enter an int, 1 or 2, Error:", err)
    else:
        if 1 > IteOrRec or 2 < IteOrRec:
            print("Please only enter an int, 1 or 2, Error: OutOfRange")
            IteOrRec = None
    

        

