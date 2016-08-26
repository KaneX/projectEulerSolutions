import sys
import math


maxSize = 41000

aIsPrime = [True] * maxSize
for i in range(2, maxSize):
    if not aIsPrime[i]:
        continue
    for j in range(2*i, maxSize, i):
        aIsPrime[j] = False

primeList = []
for i in range(2, maxSize):
    if aIsPrime[i]:
        primeList.append(i)

triangleList = [x*(x+1)//2 for x in range(1, maxSize)]
# factorNumList = [0] * maxSize
factorNumList = [1, 2]


def getFactorNum(factorInd):
    global factorNumList

    if factorInd >= len(factorNumList):
        factorNumList += [0] * (factorInd - len(factorNumList) + 1)

    if factorNumList[factorInd] == 0:
        triangleVal = triangleList[factorInd]
        currentFactorNum = 1
        for ind, prime in enumerate(primeList):
            if prime > triangleVal:
                break

            currentPower = 0
            while triangleVal % prime == 0:
                currentPower += 1
                triangleVal //= prime

            if currentPower != 0:
                currentFactorNum *= currentPower + 1

        factorNumList[factorInd] = currentFactorNum

    return factorNumList[factorInd]

T = int(input().strip())

for a0 in range(T):
    N = int(input().strip())

    i = 0
    while getFactorNum(i) <= N:
        i += 1

    print(triangleList[i])

