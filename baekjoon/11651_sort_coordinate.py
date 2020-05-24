coor = []

for i in range(int(input())):
    coor.append(list(map(int, input().split())))

coor = sorted(coor, key=lambda x: x[0])
coor = sorted(coor, key=lambda x: x[1])

for i in coor:
    print(i[0], i[1])
