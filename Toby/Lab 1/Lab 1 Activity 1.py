import numpy as np
array = int(input('How many items? '))
arr = np.ones(array, dtype = int)


for i in range (0, array):
    temp = int(input('Enter temperature ' + str(1+i) + ': '))
    arr[i] = temp
    if arr[i] < int(arr[i-1]):
        maxValue = arr[i]
    if arr[i] > int(arr[i-1]):
        minValue = arr[i]
    
print('The maximum temperature is ' + str(maxValue) + ' degrees celcius')
print('The minimum temperature is ' + str(minValue) + ' degrees celcius')
