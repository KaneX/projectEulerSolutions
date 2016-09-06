import sys
import math

maxSize = 30000

# generate a list of prime numbers
aIsPrime = [True] * maxSize
for i in range(2, maxSize):
    if not aIsPrime[i]:
        continue
    for j in range(2*i, maxSize, i):
        aIsPrime[j] = False

N = int(input().strip())
maxNum = 0
maxa = 0
maxb = 0
for a in range(-N, N+1):
    for b in range(-N, N+1):
        i = 0
        while aIsPrime[i * i + a * i + b]:
            i += 1
        if (i-1) > maxNum:
            maxNum = i - 1
            maxa = a
            maxb = b

print(maxa, maxb)