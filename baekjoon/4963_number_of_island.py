import sys
sys.setrecursionlimit(100000)


class lands:
    cnt = 0


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    maps = []
    for i in range(h):
        temp = list(map(int, input().split()))
        maps.append(temp)
    direction = [(-1, -1), (-1, 0), (-1, 1), (0, 1),
                 (1, 1), (1, 0), (1, -1), (0, -1)]
    visited = [[False for i in range(w)] for i in range(h)]
    lands.cnt = 0

    def dfs(y, x):
        visited[y][x] = True
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w:
                if not visited[ny][nx] and maps[ny][nx] != 0:
                    dfs(ny, nx)

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and maps[i][j] != 0:
                dfs(i, j)
                lands.cnt += 1

    print(lands.cnt)
