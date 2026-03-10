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


def numberConversion(num, base):
    digits = "0123456789ABCDEF"
    if num < base:
        return digits[num]
    return numberConversion(num // base, base) + digits[num % base]

'''
No refrence this is a modification of my AddBinary solution from leetcode
'''

print()
base = input_checker("What base would you like? (2-16)", 2, 16)
print()
value = input_checker("What vaule do you want to convert? (pos int only)", 0, None)

try: 
    start_time = timeit.default_timer()
    result = numberConversion(value, base)
    end_time = timeit.default_timer()

    print()
    print("Result:", result)
    print("Time:", (end_time - start_time), "\n")
except RecursionError as err:
    print("Max recursion depth reached (n is too large), Error:", err)