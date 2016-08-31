import sys
import math

N = int(input().strip())

nameList = []
for a0 in range(N):
    nameList.append(input().strip())
nameList.sort()

scoreList = []
for rank in range(len(nameList)):
    score = 0
    for ch in nameList[rank]:
        score += ord(ch) - ord('A') + 1
    score *= rank + 1
    scoreList.append(score)

Q = int(input().strip())
for a0 in range(Q):
    name = input().strip()
    print(scoreList[nameList.index(name)])
