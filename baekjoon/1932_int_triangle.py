n = int(input())

tri = []

for i in range(n):
    temp = list(map(int, input().split()))
    tri.append(temp)

for i in range(1, n):
    for j in range(len(tri[i])):
        if j == 0:
            tri[i][0] += tri[i-1][0]
        elif j == len(tri[i]) - 1:
            tri[i][j] += tri[i-1][-1]
        else:
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

print(max(tri[-1]))
