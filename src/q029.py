l = []
size = int(input().strip())
for i in range(2, size+1):
    for j in range(2, size+1):
        n = i**j
        if n not in l:
            l.append(n)

print(len(l))
