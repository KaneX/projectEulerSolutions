T = int(input().strip())

a = []
for a0 in range(T):
    N = str(input().strip())
    line = [int(x) for x in N]
    a.append(line)

sumList = []
cout = 0
for i in range(49, -1, -1):
    cin = cout
    current = 0
    for j in range(T):
        current += a[j][i]
    current += cin
    cout = current // 10
    sumList = [current % 10] + sumList

while cout > 0:
    sumList = [cout % 10] + sumList
    cout //= 10

print(*sumList[0:10], sep='')
