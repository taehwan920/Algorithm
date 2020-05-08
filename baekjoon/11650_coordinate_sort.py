N = int(input())

coors = []
for i in range(N):
    x, y = map(int, input().split())
    coors.append((x, y))

coors = sorted(coors, key=lambda x: x[1])
coors = sorted(coors, key=lambda x: x[0])

for i in coors:
    print(i[0], i[1])
