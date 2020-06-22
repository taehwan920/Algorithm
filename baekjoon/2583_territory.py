from collections import deque

m, n, k = map(int, input().split())

visited = [[1 for i in range(n)] for j in range(m)]
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for i in range(k):
    temp = list(map(int, input().split()))
    for j in range(m - temp[3], m - temp[1]):
        for l in range(temp[0], temp[2]):
            if visited[j][l] == 1:
                visited[j][l] = 0


def bfs(i, j):
    q = deque([[i, j]])
    visited[i][j] = 0
    temp = 1
    while q:
        y, x = q.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < m and 0 <= nx < n and visited[ny][nx] != 0:
                visited[ny][nx] = 0
                temp += 1
                q.append([ny, nx])
    return temp


result = []
for i in range(m):
    for j in range(n):
        if visited[i][j] == 1:
            result.append(bfs(i, j))
result.sort()
print(len(result))
for i in result:
    print(i, end=" ")
