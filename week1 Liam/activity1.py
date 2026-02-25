import numpy as np

num = int(input("How many tempretures are there?\n"))
temp = np.zeros(num, dtype = int)
for i in range (0, num):
    temp[i] = int(input("Tempreture of day " + str(i+1) + ":\n"))

min = temp[0]
max = temp[0]

for i in range (1, num):
    if min > temp[i]:
        min = temp[i]
    if max < temp[i]:
        max = temp [i]

print("The maximum tempreture was " + str(max) + "C:" )
print("The minimum tenmpreture was " + str(min) + "C:")