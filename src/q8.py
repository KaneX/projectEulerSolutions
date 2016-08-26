import sys
import math

T = int(input().strip())

for a0 in range(T):
    N, K = map(int, input().split())
    numStr = str(input().strip())
    num = [int(x) for x in numStr]

    maxProd = 0
    for i in range(N - K + 1):
        prod = 1
        for j in range(K):
            prod *= num[i+j]

        if prod > maxProd:
            maxProd = prod

    print(maxProd)
