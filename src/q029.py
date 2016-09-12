import sys
import math

MaxPower = int(math.log2(10**5)) + 2

size = int(input().strip())

num = 0
isComputed = [False] * (size + 1)
numList = [0] * MaxPower

# precompute all power possibilities for the same base, the index is the max power < 100000 we can get
# using this base
val = set()
for j in range(1, MaxPower):
    for i in range(2, size+1):
        val.add(j * i)
    numList[j] = len(val)

for i in range(2, size+1):
    if isComputed[i]:
        continue
    val = set()
    base = 1
    j = 0
    while j < MaxPower:
        j += 1
        base *= i
        if base > size:
            break
        isComputed[base] = True
    num += numList[j-1]

print(num)
