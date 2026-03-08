def factorialIterative(n):
    nFactorial = 1
    for i in range(n, 1, -1):
        nFactorial = nFactorial * i
    return nFactorial

def factorialRecursive(n):
    if n == 0:
        return 1
    else: 
        return n * factorialRecursive(n-1)

def fibonnaciIterative(n):
    fibVal = 0 
    currVal = 1
    lastVal = 0

    if n == 0: 
        fibVal = 0 
    elif n == 1: 
        fibVal = 1
    else: 
        for i in range (2, n+1):
            fibval = currVal + lastVal
            lastVal = currVal
            currVal = fibval
    return fibVal 

def fibonnaciRecursive(n):
    fibVal = 0

    if n == 0: 
        fibVal = 0 
    elif n == 1: 
        fibVal = 1
    else: 
        fibVal = fibonnaciRecursive(n-1) + fibonnaciRecursive (n-2)
    return fibVal

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
    
n = None 
while n is None:
    try: 
        print("What n vaule would you like?")
        n = int(input("Please eneter a positive int: "))
    except ValueError as err:
        print("Please only enter a posive int, Error:", err)
    else:
        if 0 > n:
            print("Please only enter a posive int, Error: OutOfRange")
            n = None  

if facOrFib == 1: 
    if IteOrRec == 1: 
        factorialIterative(n)
    else:
        factorialRecursive(n)
else: 
    if IteOrRec == 1: 
        fibonnaciIterative(n)
    else:
        fibonnaciRecursive(n)
