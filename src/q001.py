import sys
import math

T = int(input().strip())

for a0 in range(T):
    N = int(input().strip())
    n = N-1
    sum = (n//3+1) * (n//3) // 2 * 3 + \
            (n//5+1) * (n//5) // 2 * 5 - \
            (n//15+1) * (n//15) // 2 * 15
    print(int(sum))