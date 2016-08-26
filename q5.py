import sys
import math


T = int(input().strip())
primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
powerList = [0] * len(primeList)
for a0 in range(T):
    N = int(input().strip())
    powerList = [0] * len(primeList)

    for i in range(1, N+1):
        current = i
        currentPowerList = [0] * len(primeList)

        for ind, val in enumerate(primeList):
            if val > i:
                break
            while current % val == 0:
                current //= val
                currentPowerList[ind] += 1

        for ind, val in enumerate(primeList):
            if val > i:
                break
            if currentPowerList[ind] > powerList[ind]:
                powerList[ind] = currentPowerList[ind]

    result = 1
    for ind, val in enumerate(primeList):
        if val > N:
            break
        result *= val ** powerList[ind]

    print(result)
