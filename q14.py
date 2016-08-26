import sys
import math

T = int(input().strip())
#T = 1
lengthList = [0] * (15 * 10**6)
lengthList[1] = 1

maxList = [0] * 5000001

oversizeDict = dict()


def getLength(node):
    if node < len(lengthList):
        if lengthList[node] == 0:
            if node & 1 == 0:
                nextNode = node >> 1
            else:
                nextNode = 3 * node + 1
            lengthList[node] = 1 + getLength(nextNode)

        return lengthList[node]

    else:
        if node not in oversizeDict:
            if node & 1 == 0:
                nextNode = node >> 1
            else:
                nextNode = 3 * node + 1
            oversizeDict[node] = 1 + getLength(nextNode)

        return oversizeDict[node]

maxInd = 1
for i in range(1, 5000001):
    if getLength(i) >= lengthList[maxInd]:
        maxInd = i
    maxList[i] = maxInd

for a0 in range(T):
    #N = 1000000
    N = int(input().strip())


    print(maxList[N])
