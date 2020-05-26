import sys
from collections import deque


def bfs(y, x):
    q = deque([[y, x]])
    melt_q = deque()
    visited[y][x] = True
    while q:
        y, x = q.popleft()
        melt_cnt = 0
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx]:
                if ocean[ny][nx] != 0:
                    visited[ny][nx] = True
                    q.append([ny, nx])
                else:
                    melt_cnt += 1
        if melt_cnt:
            melt_q.append([y, x, melt_cnt])
    return melt_q

# def dfs(y, x):
#   visited[y][x] = True
#   melt_cnt = 0
#   for dy, dx in direction:
#     ny, nx = y + dy, x + dx
#     if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx]:
#       if ocean[ny][nx] > 0:
#         dfs(ny, nx)
#       else:
#         melt_cnt += 1


input = sys.stdin.readline
h, w = map(int, input().split())
ocean = []
for i in range(h):
    ocean.append(list(map(int, input().split())))
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
years = 0
while True:
    visited = [[False for i in range(w)] for i in range(h)]
    cnt = 0
    for i in range(1, h-1):
        for j in range(1, w-1):
            if not visited[i][j] and ocean[i][j] > 0:
                cnt += 1
                melt = bfs(i, j)
                while melt:
                    my, mx, m = melt.popleft()
                    ocean[my][mx] = max(ocean[my][mx]-m, 0)
    if cnt == 0:
        print(0)
        break
    if cnt > 1:
        print(years)
        break
    years += 1
