a, b = input().split()
where = []
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            where = [i, j]
            break
    if where:
        break

result = [['.' for i in range(len(a))] for i in range(len(b))]
for i in range(len(b)):
    result[i][where[0]] = b[i]
result[where[1]] = list(a)

for i in result:
    print(''.join(i))
