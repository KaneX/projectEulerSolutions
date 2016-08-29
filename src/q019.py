import sys
import math


def zeller(y, m, d):
    if m < 3:
        m += 12
        y -= 1
    h = (d + (13 * (m + 1)) // 5 + y % 100 + (y % 100) // 4 + (y // 100) // 4 - 2 * (y // 100)) % 7
    return (h + 5) % 7 + 1

matchSumList = [[0 for x in range(12)] for y in range(400)]

matchSumList[0][0] = 1
for i in range(400):
    for j in range(1, 13):
        if i == 0 and j == 1:
            continue
        if zeller(i+1900, j, 1) == 1:
            matchSumList[i][j-1] = matchSumList[i][j-2] + 1 if j > 1 else matchSumList[i-1][11] + 1
        else:
            matchSumList[i][j-1] = matchSumList[i][j-2] if j > 1 else matchSumList[i-1][11]

cntIn400Yrs = 684

T = int(input().strip())

for a0 in range(T):
    Y1, M1, D1 = map(int, input().split())
    Y2, M2, D2 = map(int, input().split())

    cnt1 = (Y1 - 1900) // 400 * cntIn400Yrs
    Y1 -= (Y1 - 1900) // 400 * 400
    cnt1 += matchSumList[Y1 - 1900][M1 - 1]

    if zeller(Y1, M1, D1) == 1:
        cnt1 -= 1

    cnt2 = (Y2 - 1900) // 400 * cntIn400Yrs
    Y2 -= (Y2 - 1900) // 400 * 400
    cnt2 += matchSumList[Y2 - 1900][M2 - 1]

    print(cnt2 - cnt1)
