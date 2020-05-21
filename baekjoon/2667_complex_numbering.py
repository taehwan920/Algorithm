import sys
from collections import deque

n = int(sys.stdin.readline())
house = []
visited = [[False for i in range(n)] for i in range(n)]
result = []
for _ in range(n):
    house.append(list(map(int, input())))


def bfs(x, y):
    q = deque([[x, y]])
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited[x][y] = True
    # 이 행과 이 윗 행의 코드가 누락되면 단지내 집 수가 1일 경우 탐색을 하지 않고 넘어가기때문에 집 수가 0으로 나오는 오류가 있음.
    count = 1
    while q:
        t_x, t_y = q.popleft()
        for dx, dy in direction:
            nx, ny = t_x + dx, t_y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if house[nx][ny] and not visited[nx][ny]:
                count += 1
                visited[nx][ny] = True
                q.append([nx, ny])
    return count


for i in range(n):
    for j in range(n):
        if house[i][j] and not visited[i][j]:
            result.append(bfs(i, j))

result.sort()
print(len(result))
for i in result:
    print(i)
