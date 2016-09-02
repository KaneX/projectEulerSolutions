import sys
import math

maxSize = 28123

# generate a list of prime numbers
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


def isAbundant(val):
    if aIsPrime[val]:
        return False
    current = val
    primeDivisorList = []
    for prime in primeList:
        if prime > current:
            break
        power = 0
        while current % prime == 0:
            power += 1
            current //= prime
        if power > 0:
            primeDivisorList.append([prime, power])

    sumOfDivisors = 1
    for divisor in primeDivisorList:
        sumOfDivisors *= (1 - divisor[0] ** (divisor[1] + 1)) // (1 - divisor[0])
    sumOfDivisors -= val
    if sumOfDivisors > val:
        return True
    else:
        return False


T = int(input().strip())
for a0 in range(T):
    N = int(input().strip())
    if N > 28123:
        print('YES')
        continue

    rtn = False
    for i in range(12, N // 2 + 1):
        if isAbundant(i) and isAbundant(N - i):
            rtn = True
            break
    print('YES' if rtn else 'NO')
