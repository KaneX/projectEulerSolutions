import math

lineNum = 20

a = []
for i in range(lineNum):
    line = [int(x) for x in input().split()]
    a.append(line)

# -
maxProd = 0
for i in range(lineNum):
    for j in range(lineNum-3):
        currentProd = a[i][j] * a[i][j+1] * a[i][j+2] * a[i][j+3]
        if currentProd > maxProd:
            maxProd = currentProd

# |
for i in range(lineNum-3):
    for j in range(lineNum):
        currentProd = a[i][j] * a[i+1][j] * a[i+2][j] * a[i+3][j]
        if currentProd > maxProd:
            maxProd = currentProd

# \
for i in range(lineNum-3):
    for j in range(lineNum-3):
        currentProd = a[i][j] * a[i+1][j+1] * a[i+2][j+2] * a[i+3][j+3]
        if currentProd > maxProd:
            maxProd = currentProd

# /
for i in range(lineNum-3):
    for j in range(3, lineNum):
        currentProd = a[i][j] * a[i+1][j-1] * a[i+2][j-2] * a[i+3][j-3]
        if currentProd > maxProd:
            maxProd = currentProd

print(maxProd)
