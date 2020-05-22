import heapq

h, w = map(int, input().split())
cave = []
water = []
start = []
maps = []
visited = [[[False, False] for i in range(w)] for i in range(h)]

for i in range(h):
    temp = list(input())
    maps.append(temp)
    for j in range(w):
        if temp[j] == "D":
            cave = [i, j]
        if temp[j] == "*":
            water.append([i, j])
        if temp[j] == "S":
            start = [0, i, j]


def bfs():
    global water
    q = []
    heapq.heappush(q, start)
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        cnt, y, x = heapq.heappop(q)
        visited[y][x][0] = True
        if [y, x] == cave:
            return cnt
        temp_w = []
        while water:
            wy, wx = water.pop(0)
            visited[wy][wx][1] = True
            for dy, dx in direction:
                nwy, nwx = wy + dy, wx + dx
                if 0 <= nwy < h and 0 <= nwx < w and not visited[nwy][nwx][1]:
                    if maps[nwy][nwx] != "X" and maps[nwy][nwx] != "D":
                        visited[nwy][nwx][0], visited[nwy][nwx][1] = True, True
                        temp_w.append([nwy, nwx])
        water = temp_w
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx][0]:
                if maps[ny][nx] != "X" and [ny, nx] not in water:
                    heapq.heappush(q, [cnt+1, ny, nx])
    return -1


result = bfs()
print('KAKTUS') if result == -1 else print(result)
# 로직은 맞지만 시간초과. 다시 풀어볼것
