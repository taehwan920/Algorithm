from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def RG_weak(y, x):
    q = deque([[y, x]])
    visited[y][x][0] = True
    while q:
        yy, xx = q.popleft()
        for dy, dx in direction:
            ny, nx = yy + dy, xx + dx
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx][0]:
                if board[y][x] == "B":
                    if board[ny][nx] == "B":
                        visited[ny][nx][0] = True
                        q.append([ny, nx])
                else:
                    if board[ny][nx] != "B":
                        visited[ny][nx][0] = True
                        q.append([ny, nx])


def dfs(y, x):
    visited[y][x][1] = True
    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx][1]:
            if board[y][x] == board[ny][nx]:
                dfs(ny, nx)


n = int(input())
board = []
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(n):
    board.append(list(input()))

visited = [[[False, False] for i in range(n)] for i in range(n)]
rgw = 0
norm = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j][0]:
            RG_weak(i, j)
            rgw += 1
        if not visited[i][j][1]:
            dfs(i, j)
            norm += 1
print(norm, rgw)

# bfs 탐색 문제가 시간초과가 뜨면 dfs로 할 것.
