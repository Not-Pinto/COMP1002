import timeit

def factorial_iterative(n):
    nFactorial = 1
    for i in range(n, 1, -1):
        nFactorial = nFactorial * i
    return nFactorial


def factorial_recursive(n):
    if n == 0:
        return 1
    else: 
        return n * factorial_recursive(n - 1)


def fibonacci_iterative(n):
    fibVal = 0 
    currVal = 1
    lastVal = 0

    if n == 0: 
        fibVal = 0 
    elif n == 1: 
        fibVal = 1
    else: 
        for i in range (2, n + 1):
            fibVal = currVal + lastVal
            lastVal = currVal
            currVal = fibVal
    return fibVal 


def fibonacci_recursive(n):
    fibVal = 0

    if n == 0: 
        fibVal = 0 
    elif n == 1: 
        fibVal = 1
    else: 
        fibVal = fibonacci_recursive(n - 1) + fibonacci_recursive (n - 2)
    return fibVal


def input_checker(message, min_output, max_output):
    output = None
    while output is None:
        print(message)
        try:
            output = int(input("Please eneter an int: "))
            if max_output is None:
                if output < min_output:
                    print("Please enter an int in range:")
                    output = None
            elif output < min_output or output > max_output:
                 print("Please enter an int in range:")
                 output = None
        except ValueError:
            print("Please only input integers")
    return output


fac_or_fib = input_checker("Would you like to see Factorial(1) or Fibonnaci"
                           " (2)?", 1, 2)
ite_or_rec = input_checker("Would you like to see Iterative(1) or Recursive"
                           " (2)?", 1, 2)
n = input_checker("What n vaule would you like?", 0, None)

print()
try: 
    if fac_or_fib == 1: 
        if ite_or_rec == 1: 
            algorithm = factorial_iterative
        else:
            algorithm = factorial_recursive
    else: 
        if ite_or_rec == 1: 
            algorithm = fibonacci_iterative
        else:
            algorithm = fibonacci_recursive

    start_time = timeit.default_timer()
    result = algorithm(n)
    end_time = timeit.default_timer()

    try:
        print ("\nResult:", result)
    except ValueError as err:
        print("Result is too large to display, Error:", err)
    print("Time:", (end_time - start_time), "\n")
    
except RecursionError as err:
    print("Recursion depth exceeded as n is too large, Error:", err)
