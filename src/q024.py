import sys
import math

chList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
factList = [math.factorial(x) for x in range(13)]

T = int(input().strip())

for a0 in range(T):
    N = int(input().strip()) - 1

    chRemainList = list(chList)
    rtn = ''

    for i in range(12, -1, -1):
        currentNo = N // factList[i]
        rtn += chRemainList[currentNo]
        del(chRemainList[currentNo])
        N %= factList[i]

    print(rtn)
