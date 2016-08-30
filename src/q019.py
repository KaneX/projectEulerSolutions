import sys
import math
import re


def zeller(y, m, d):
    """
    Zeller's congruence
    :param y: year
    :param m: month
    :param d: day
    :return: current date of the week, 1 for Monday, 2 for Tuesday ...
    """
    if m < 3:
        m += 12
        y -= 1
    h = (d + (13 * (m + 1)) // 5 + y % 100 + (y % 100) // 4 + (y // 100) // 4 - 2 * (y // 100)) % 7
    return (h + 5) % 7 + 1


def isLeap(y):
    if y % 400:
        return True
    elif y % 100:
        return False
    elif y % 4:
        return True
    else:
        return False


T = int(input().strip())

for a0 in range(T):
    line = input().strip()
    intLine = re.sub('[^\d ]', '', line)
    Y1, M1, D1 = map(int, intLine.split())
    line = input().strip()
    intLine = re.sub('[^\d ]', '', line)
    Y2, M2, D2 = map(int, intLine.split())

    cnt = 0
    for i in range(Y1, Y2 + 1):
        for j in range(12):
            if zeller(i, j+1, 1) == 7:
                cnt += 1
    for j in range(1, M1 + 1):
        if zeller(Y1, j, 1) == 7:
            cnt -= 1
    if D1 == 1 and zeller(Y1, M1, D1) == 7:
        cnt += 1
    for j in range(M2 + 1, 13):
        if zeller(Y2, j, 1) == 7:
            cnt -= 1

    print(cnt)
