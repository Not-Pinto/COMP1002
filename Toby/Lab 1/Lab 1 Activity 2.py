import numpy as np

date = np.empty(365, dtype = "U10")
temp = np.empty(365, dtype = int)

with open ('temperatures_365_days.csv', mode = 'r') as values:
    next(values)

    a = 0
    for line in values:
        parts = line.strip().split(",")
        date[a] = parts[0]
        temp[a] = parts[1]
        a += 1


maxT = temp[0]
maxD = date[0]
minT = temp[0]
minD = date[0]

for i in range (1,365):
    if minT > temp[i]:
        minT = temp [i]
        minD = date[i]
    if maxT < temp[i]:
        maxT = temp[i]
        maxD = date[i]

print(str(maxD) + " had the hottest day of " + str(maxT) +" degrees")
print(str(minD) + " had the coldest day of " + str(minT) + " degrees")
