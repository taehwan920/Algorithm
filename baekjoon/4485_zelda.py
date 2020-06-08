import heapq

cnt = 0
while True:
    cnt += 1
    n = int(input())
    if n == 0:
        break
    dungeon = []
    distance = [[1e9] * n for i in range(n)]
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for i in range(n):
        dungeon.append(list(map(int, input().split())))

    def djik():
        q = []
        heapq.heappush(q, [dungeon[0][0], 0, 0])
        distance[0][0] = dungeon[0][0]
        while q:
            dist, y, x = heapq.heappop(q)
            if dist > distance[y][x]:
                continue
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < n:
                    # bfs/dfs 문제 풀때 맨날 쓰던 이 조건을 빼먹어서 답이 계속 틀리게 나왔었다.
                    # 잘 생각하면서 풀기
                    cost = dungeon[ny][nx] + dist
                    if cost < distance[ny][nx]:
                        distance[ny][nx] = cost
                        heapq.heappush(q, [cost, ny, nx])

    djik()
    print(f'Problem {cnt}: {distance[n-1][n-1]}')
