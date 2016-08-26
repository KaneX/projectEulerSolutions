import sys
import math

T = int(input().strip())

for a0 in range(T):
    N = int(input().strip())

    rtn = -1
    for a in range(1, N//3):
        b = (N**2 - 2*a*N) // (2*N - 2*a)
        c = N - a - b
        if a < b < c and a**2+b**2 == c**2 and a*b*c > rtn:
            rtn = a*b*c

    print(rtn)
