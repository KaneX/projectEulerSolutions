size = int(input().strip())
num = 0
isComputed = [False for x in range(0, size+1)]


for i in range(2, size+1):
    if isComputed[i]:
        continue
    val = set()
    base = 1
    for j in range(1, 15):    # 2**14 > 100000
        base *= i
        if base > size:
            break
        isComputed[base] = True
        for k in range(2, size+1):
            n = j * k

            if n not in val:
                val.add(n)
                num += 1

    print(val)

print(num)
