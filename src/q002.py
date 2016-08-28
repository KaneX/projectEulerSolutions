import sys
import math

T = int(input().strip())
fib = [2, 1]
sum = [2, 0]
for a0 in range(T):
    N = int(input().strip())
    
    if N == 1:
        print(1)
        continue
    if N == 2:
        print(2)
        continue

    if fib[0] < N:
        while fib[0] < N:
            fib.insert(0, fib[0]+fib[1])
            if (fib[0] % 2 == 0):
                sum.insert(0, fib[0] + sum[0])
            else:
                sum.insert(0, sum[0])
        solve = sum[1]
    else:
        for i in range(len(fib)):
            if fib[i] < N:
                solve = sum[i]
                break

    print(solve)