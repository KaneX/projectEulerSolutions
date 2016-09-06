import sys
import math

maxSize = 10001

# generate a list of prime numbers
aIsPrime = [True] * maxSize
for i in range(2, maxSize):
    if not aIsPrime[i]:
        continue
    for j in range(2*i, maxSize, i):
        aIsPrime[j] = False

primeList = []
for i in range(3, maxSize):
    if aIsPrime[i] and i != 5:
        primeList.append(i)

lengthList = [0] * maxSize
T = int(input().strip())
for a0 in range(T):
    N = int(input().strip())
    maxLength = 0
    maxPrime = 2
    for prime in primeList:
        if prime >= N:
            break
        if lengthList[prime] == 0:
            length = 1
            divisor = 10
            while divisor % prime != 1:
                length += 1
                divisor = divisor * 10 % prime  # mod prime is crucial, otherwise it will get time out.
            lengthList[prime] = length
        if lengthList[prime] > maxLength:
            maxLength = lengthList[prime]
            maxPrime = prime

    print(maxPrime)
