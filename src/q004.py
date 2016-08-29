import sys
import math


def isPalindrome(val):
    if val // 100000 == val % 10 and \
       val // 10000 % 10 == val % 100 // 10 and \
       val // 1000 % 10 == val % 1000 // 100:

        return True
    else:
        return False


def generatePalindromeList():
    rtn = [101101]

    for i in range(100, 1000):
        for j in range(i, 1000):
            result = i * j
            if result >= 1000000:
                break
            if result <= 101101:
                continue

            if isPalindrome(result):
                # print(result)
                inserted = False
                for ind, val in enumerate(rtn):
                    if val > result:
                        rtn.insert(ind, result)
                        inserted = True
                        break

                if not inserted:
                    rtn.append(result)

    return rtn

T = int(input().strip())
palindromeList = generatePalindromeList()
# print(palindromeList)
for a0 in range(T):
    N = int(input().strip())

    maxPalindrome = palindromeList[-1]
    for i in range(len(palindromeList)):
        if palindromeList[i] >= N:
            maxPalindrome = palindromeList[i-1]
            break

    print(maxPalindrome)
