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

# solution to Q23 on hackerrank.com
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

'''
# solution to Q23 on projecteuler.net
abundantList = []
for i in range(12, maxSize - 11):
    if isAbundant(i):
        abundantList.append(i)

candidateList = [x for x in range(maxSize + 1)]
for i in range(len(abundantList)):
    for j in range(i, len(abundantList)):
        if (abundantList[i] + abundantList[j]) < len(candidateList):
            candidateList[abundantList[i] + abundantList[j]] = 0
        else:
            break
print(sum(candidateList))
'''
