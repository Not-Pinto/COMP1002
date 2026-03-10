import timeit

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


def gcd(first_value, second_value):
    if second_value == 0: 
        return first_value
    return gcd(second_value, first_value % second_value)

'''
Reference:
GeeksforGeeks. 2025. "Euclidean Algorithms (Basic and Extended)."
https://www.geeksforgeeks.org/dsa/euclidean-algorithms-basic-and-extended/

used from lines 25 to 28
'''

print()
first_value = input_checker("First value, (positive int only)", 0, None)
print()
second_value = input_checker("Second value, (positive int only)", 0, None)
print()

start_time = timeit.default_timer()
result = gcd(first_value, second_value)
end_time = timeit.default_timer()

print("Result:", result)
print("Time:", (end_time - start_time), "\n")