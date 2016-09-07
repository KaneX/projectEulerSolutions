import sys
import math

mod = 10 ** 9 + 7

T = int(input().strip())

for a0 in range(T):
    N = int(input().strip())
    k = (N - 1) // 2 % mod
    if k == 0:
        s = 1
    else:
        # compute Sigma 4*k**2 + k + 1
        s = (1 + 4 * (2 * k * (k+1) * (2*k+1) // 3 % mod + (k+1) * k // 2 % mod + k)) % mod

    print(s)
