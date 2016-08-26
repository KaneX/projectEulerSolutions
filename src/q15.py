import sys
import math

T = int(input().strip())
for a0 in range(T):
    N, M = map(int, input().split())

    # print(routeList[N][M] % int(1e9 + 7))
    print(math.factorial(M+N) // math.factorial(M) // math.factorial(N) % int(1e9 + 7))
