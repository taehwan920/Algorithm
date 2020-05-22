import heapq

n, m = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(input()))


def bfs(start):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False for i in range(m)] for j in range(n)]
    q = []
    heapq.heappush(q, start)
    nominee = []
    while q:
        cnt, y, x = heapq.heappop(q)
        nominee.append(cnt)
        visited[y][x] = True
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and maps[ny][nx] == "L":
                    visited[ny][nx] = True
                    heapq.heappush(q, [cnt + 1, ny, nx])
    return max(nominee)


result = []

for i in range(n):
    for j in range(m):
        if maps[i][j] == "L":
            result.append(bfs([0, i, j]))

print(max(result))
# 발견 : bfs에서 최단 경로를 알아내고싶으면 heap으로 큐를 구현할 것.
# 이번 로직은 각 육지마다 가장 먼 노드와의 최단거리를 저장해두고 그중 가장 큰 것을 제출함.
