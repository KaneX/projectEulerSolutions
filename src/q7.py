import sys
import math

T = int(input().strip())

maxSize = 200000

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

for a0 in range(T):
    N = int(input().strip())

    print(primeList[N-1])
