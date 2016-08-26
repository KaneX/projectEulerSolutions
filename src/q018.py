import sys
import math

"""
This solution can be used for both Q18 and Q67 on projecteuler.net
"""

T = int(input().strip())

for a0 in range(T):
    N = int(input().strip())

    triangleList = []
    for i in range(N):
        line = [int(x) for x in input().split()]
        triangleList.append(line)

    maxRouteList = [[triangleList[0][0]]]
    for i in range(1, N):
        currentLine = []
        for j in range(0, i+1):
            currentMax = 0
            if j - 1 >= 0:
                currentRoute = triangleList[i][j] + maxRouteList[i-1][j-1]
                if currentRoute > currentMax:
                    currentMax = currentRoute
            if len(maxRouteList[i-1]) > j:
                currentRoute = triangleList[i][j] + maxRouteList[i-1][j]
                if currentRoute > currentMax:
                    currentMax = currentRoute
            currentLine.append(currentMax)
        maxRouteList.append(currentLine)

    print(max(maxRouteList[N-1]))
