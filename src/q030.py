import sys
import math

N = int(input().strip())

rtn = 0
for i in range(10**(N-1), 10**N):
    current = i
    s = 0
    while current != 0:
        s += (current % 10) ** N
        current //= 10
    if s == i:
        rtn += s
        print(i)

print(rtn)
