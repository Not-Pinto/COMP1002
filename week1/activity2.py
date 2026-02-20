import numpy as np 

dates = np.zeros(365)
temp = np.zeros(365)

with open("temperatures_365_days.csv", "r") as data:
    next(data)

    for line in data:
        temp[line] = int(line.strip().split()[1])

print(temp)