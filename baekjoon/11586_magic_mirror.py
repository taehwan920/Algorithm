n = int(input())
mirror = []

for i in range(n):
    mirror.append(list(input()))

psy = int(input())

if psy == 1:
    for i in mirror:
        print(''.join(i))
elif psy == 2:
    for i in mirror:
        for j in range(n-1, -1, -1):
            print(i[j], end="")
        print()
else:
    for i in range(n-1, -1, -1):
        print(''.join(mirror[i]))
