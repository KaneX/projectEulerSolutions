import sys
import math

maxSize = 100000


def findAmicable(a):
    aFactors = []
    for i in range(1, int(math.sqrt(a)) + 1):
        if a % i == 0:
            aFactors.append(i)
            if a // i != i and a // i != a:
                aFactors.append(a // i)

    b = sum(aFactors)
    bFactors = []
    for i in range(1, int(math.sqrt(b)) + 1):
        if b % i == 0:
            bFactors.append(i)
            if b // i != i and b // i != b:
                bFactors.append(b // i)

    if a != b and sum(bFactors) == a:
        return b
    else:
        return -1

amicableList = []
sumList = [0] * (maxSize + 1)
for a in range(2, maxSize + 1):
    if a in amicableList:
        continue
    b = findAmicable(a)
    if b != -1:
        amicableList.append(a)
        amicableList.append(b)

amicableList.sort()
# print(amicableList)

T = int(input().strip())

for a0 in range(T):
    N = int(input().strip())
    s = 0
    for i in range(len(amicableList)):
        if amicableList[i] < N:
            s += amicableList[i]

    print(s)
