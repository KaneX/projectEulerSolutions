import sys
import math

T = int(input().strip())
prime = [2, 3, 5, 7]
for a0 in range(T):
    N = int(input().strip())

    while N % 2 == 0:
        N //= 2
    if N == 1:
        print(2)

    maxPrime = 3
    n = N
    for val in range(3, int(math.sqrt(N))+1, 2):
        if n % val == 0:
            maxPrime = val
        while n % val == 0:
            n //= val

    if n == 1:
        print(maxPrime)
    else:
        print(n)
