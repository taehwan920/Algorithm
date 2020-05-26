from collections import deque
import sys
sys.setrecursionlimit(100000)

n = int(input())
board = []
MAX = 0
for i in range(n):
    temp = list(map(int, input().split()))
    board.append(temp)
    MAX = max(MAX, max(temp))


def bfs(y, x):
    q = deque([[y, x]])
    visited[q[0][0]][q[0][1]] = True
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        y, x = q.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n:
                if not visited[ny][nx] and board[y][x] > flood:
                    q.append([ny, nx])


def dfs(y, x):
    visited[y][x] = True
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < n:
            if not visited[ny][nx] and board[y][x] > flood:
                dfs(ny, nx)


result = 0

for flood in range(MAX):
    visited = [[False for i in range(n)] for i in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] > flood:
                visited[i][j] = True
                # bfs(i, j)
                dfs(i, j)
                cnt += 1
    result = max(result, cnt)

print(result)

# 처음에 bfs로 풀었지만 메모리 초과가 떠서 result를 배열에서 정수 변수로 바꾸어 보았지만 그래도 실패.
# 그래서 dfs로 풀어보니 이번엔 런타임 에러가 떠서 이유를 알아보니 재귀 콜 스택 제한을 초과한게 원인이라 재귀 콜 스택 제한을 10만으로 늘렸더니 해결되었다.
# dfs가 bfs보단 보통 빠름.
