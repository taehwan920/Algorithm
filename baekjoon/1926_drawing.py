# from collections import deque
# import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

h, w = map(int, input().split())
board = []
visited = [[0 for i in range(w)] for i in range(h)]

for i in range(h):
    board.append(list(map(int, input().split())))


class Size:
    val = 1
    many = 0


direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def dfs(y, x):
    visited[y][x] = 1
    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if ny < 0 or ny >= h or nx < 0 or nx >= w:
            continue
        if visited[ny][nx] or board[ny][nx] == 0:
            continue
        Size.val += 1
        dfs(ny, nx)


result = 0

for i in range(h):
    for j in range(w):
        if visited[i][j] or board[i][j] == 0:
            continue
        Size.val = 1
        dfs(i, j)
        Size.many += 1
        result = Size.val if Size.val > result else result

print(Size.many)
print(result)
