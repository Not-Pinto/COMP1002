import numpy as np 

date = np.empty(365, dtype = "U10")
temp = np.zeros(365, dtype = int)

with open("COMP1002/week1/temperatures_365_days.csv", "r") as data:
    next(data)

    for i, line in enumerate(data):
        date[i] = str(line.strip().split(",")[0])
        temp[i] = int(line.strip().split(",")[1])

maxT = temp[0]
maxD = date[0]
minT = temp[0]
minD = date[0]

for i in range (1, 365):
    if minT > temp[i]:
        minT = temp[i]
        minD = date[i]
    if maxT < temp[i]:
        maxT = temp[i]
        maxD = date[i]

print(maxD + " had the hottest day of " + str(maxT) + "C:")
print(minD + " had the hottest day of " + str(minT) + "C:")