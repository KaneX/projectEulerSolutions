import sys
import math

wordList = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve',
            'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
tensList = ['Zero', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']


def writeHundred(val):
    rtn = ''

    if val >= 100:
        rtn += wordList[val // 100] + ' Hundred'
        val %= 100
        if val != 0:
            # projecteuler.net
            #rtn += ' and '
            # hackerrank.com
            rtn += ' '
        else:
            val = -1
    if val > 19:
        rtn += tensList[val // 10]
        val %= 10
        if val != 0:
            rtn += ' ' + wordList[val]
    elif val >= 0:
        rtn += wordList[val]

    return rtn

# solution to ProjectEuler+ on hackerrank.com
T = int(input().strip())
for a0 in range(T):
    N = int(input().strip())

    rtnStr = ''
    if N == 1e12:
        rtnStr += 'One Trillion'
        N = -1
    if N >= 1e9:
        rtnStr += writeHundred(N // int(1e9)) + ' Billion'
        N %= int(1e9)
        if N != 0:
            rtnStr += ' '
        else:
            N = -1
    if N >= 1e6:
        rtnStr += writeHundred(N // int(1e6)) + ' Million'
        N %= int(1e6)
        if N != 0:
            rtnStr += ' '
        else:
            N = -1
    if N >= 1000:
        rtnStr += writeHundred(N // 1000) + ' Thousand'
        N %= 1000
        if N != 0:
            rtnStr += ' '
        else:
            N = -1
    if N >= 0:
        rtnStr += writeHundred(N)

    print(rtnStr)


'''
# solution to Q17 on projecteuler.net

total = 0
for i in range(1, 1000):

    word = writeHundred(i)
    print(word)
    total += len(word.replace(' ', ''))

print(total+11)
'''
