import sys
import math


Golden = (1 + 5 ** 0.5) / 2
preComp1 = math.log10(Golden)
preComp2 = 1 - math.log10(5 ** 0.5)

T = int(input().strip())

for a0 in range(T):
    N = int(input().strip())
    # use a formula to compute the length of Fibonacci numbers
    # ref: http://www.had2know.com/academics/number-digits-length-fibonacci-number.html
    print(math.ceil((N - preComp2) / preComp1))
