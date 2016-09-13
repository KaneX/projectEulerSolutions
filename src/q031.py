import sys
import math

maxSize = 200
coinList = [1, 2, 5, 10, 20, 50, 100, 200]
choiceList = [[0 for i in range(maxSize+1)] for j in range(len(coinList)+1)]

for i in range(len(coinList)+1):
    choiceList[i][0] = 1

for i in range(1, len(coinList)+1):
    for j in range(1, maxSize+1):
        for k in range(j // coinList[i-1] + 1):
            choiceList[i][j] += choiceList[i - 1][j - k * coinList[i - 1]]

T = int(input().strip())
for a0 in range(T):
    N = int(input().strip())
    print(choiceList[len(coinList)][N])
