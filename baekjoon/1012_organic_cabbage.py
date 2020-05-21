import sys
sys.setrecursionlimit(100000)


def bfs(x, y):
    q = [[x, y]]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        temp = q.pop(0)
        t_x, t_y = temp[0], temp[1]
        if not visited[t_x][t_y]:
            visited[t_x][t_y] = True
            for dx, dy in directions:
                nx, ny = t_x + dx, t_y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if farm[nx][ny] and not visited[nx][ny]:
                    q.append([nx, ny])


def dfs(x, y):
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if farm[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)


for _ in range(int(sys.stdin.readline())):
    m, n, k = map(int, input().split())
    farm = [[0] * m for __ in range(n)]
    visited = [[False] * m for __ in range(n)]
    for i in range(k):
        y, x = map(int, sys.stdin.readline().split())
        farm[x][y] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            if farm[i][j] and not visited[i][j]:
                # bfs(i, j)
                dfs(i, j)
                result += 1
    print(result)

# 로직1. 모든 배열을 순회하면서 1을 발견하면 dfs/bfs로 그 1과 연결된 모든 1을 전부 visited 상태로 만들어주고, 그 한번의 탐색으로 모두 visited가 된 1들은 한 뭉치 이므로 뭉치 개수 합인 result에 1을 더해준다.
# 로직2. directions 배열에 상하좌우 이동하는 경우를 담아주고, directions를 순회하면서 새 x, y를 구한 뒤 각 x, y가 0 이하 혹은 최대값 이상이 되면 idxError가 뜨므로 그경우를 제외한 모든 것에 대해 또 탐색을 진행.
