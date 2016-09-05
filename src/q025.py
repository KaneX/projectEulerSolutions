import sys
import math


Golden = (1 + 5 ** 0.5) / 2
preComp = 1 - math.log10(5 ** 0.5)

firstEncounterList = [0, 1]
i = 1
while len(firstEncounterList) <= 5000:
    i += 1
    # use a formula to compute the length of Fibonacci numbers
    # ref: http://www.had2know.com/academics/number-digits-length-fibonacci-number.html
    if math.floor(i * math.log10(Golden) + preComp) >= len(firstEncounterList):
        firstEncounterList.append(i)

# print(firstEncounterList)

T = int(input().strip())

for a0 in range(T):
    N = int(input().strip())
    print(firstEncounterList[N])
