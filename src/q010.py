import sys
import math

T = int(input().strip())

maxSize = 2100000

aIsPrime = [True] * maxSize
for i in range(2, maxSize):
    if not aIsPrime[i]:
        continue
    for j in range(2*i, maxSize, i):
        aIsPrime[j] = False

primeList = []
sumList = []
for i in range(2, maxSize):
    if aIsPrime[i]:
        primeList.append(i)
        if not sumList:
            sumList.append(i)
        else:
            sumList.append(sumList[-1]+i)

for a0 in range(T):
    N = int(input().strip())

    ind = len(primeList) // 2
    gap = math.ceil(len(primeList) / 2)
    while not (primeList[ind] <= N < primeList[ind+1]):
        gap = math.ceil(gap / 2)
        if primeList[ind] > N:
            ind -= gap
        else:
            ind += gap

    print(sumList[ind])
