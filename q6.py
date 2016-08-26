import sys
import math


T = int(input().strip())

for a0 in range(T):
    N = int(input().strip())

    sumOfSquare = N * (N+1) * (2*N+1) // 6
    squareOfSum = (N * (N+1) // 2) ** 2

    print(abs(sumOfSquare - squareOfSum))
