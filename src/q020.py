import sys
import math


def mul(aList, b):
    bList = [int(x) for x in str(b)]
    res = [0] * (len(aList) + len(bList))

    for i in range(len(bList) - 1, -1, -1):
        temp = [0] * (len(aList) + 1)
        for j in range(len(aList) - 1, -1, -1):
            temp[j+1] += aList[j] * bList[i]
            if temp[j+1] > 9:
                temp[j] = temp[j+1] // 10
                temp[j+1] %= 10
        for j in range(len(aList), -1, -1):
            res[i+j] += temp[j]
            if res[i+j] > 9:
                res[i+j-1] += res[i+j] // 10
                res[i+j] %= 10

    if res[0] == 0:
        del(res[0])

    return res

factList = [[1], [1]]

for i in range(1, 1000):
    factList.append(mul(factList[i], (i + 1)))

T = int(input().strip())

for a0 in range(T):
    N = int(input().strip())
    print(sum(factList[N]))

