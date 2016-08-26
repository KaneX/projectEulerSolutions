import sys
import math

maxN = 10000

T = int(input().strip())
for a0 in range(T):
    N = int(input().strip())
    result = 2 ** N
    line = [int(x) for x in str(result)]
    print(sum(line))