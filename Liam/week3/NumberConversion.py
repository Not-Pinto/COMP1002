import numpy as np
import timeit

def input_checker(message, min_output , max_output):
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
    digits = np.array(['0','1','2','3','4','5','6','7',
                       '8','9','A','B','C','D','E','F'])
    while num < base:
        return digits[num]
    return numberConversion(num // base, base) + digits[num % base]

'''
No refrence this is a modification of my AddBinary solution from leetcode
'''

print()
base = input_checker("What base would you like? (2-16)", 2, 16)
print()
value = input_checker("What vaule do you want to convert? (pos int only)", 0, None)

startTime = timeit.default_timer()
result = numberConversion(value, base)
endTime = timeit.default_timer()

print()
print("Result:", result)
print("Time:", (endTime - startTime), "\n")