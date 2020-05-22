import heapq
from collections import deque

n, m = map(int, input().split())
maps = []

for _ in range(n):
    temp = list(map(int, list(input())))
    maps.append(temp)

visited = [[False for i in range(m)] for i in range(n)]
room, chance = 1, 1


def bfs():
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque([[0, 0, room, chance]])
    visited[0][0] = True
    while q:
        ty, tx, troom, tch = q.popleft()
        if ty == n-1 and tx == m-1:
            return troom
        for dy, dx in direction:
            ny, nx = ty + dy, tx + dx
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if not visited[ny][nx]:
                if maps[ny][nx] == 0:
                    visited[ny][nx] = True
                    q.append([ny, nx, troom+1, tch])
                elif tch:
                    visited[ny][nx] = True
                    q.append([ny, nx, troom+1, tch-1])
    return -1


print(bfs())
# 위에건 내가 짠 코드. 근데 이건 최소 경로 안에 1이 두번있으면 실패가 떠버림. 즉 마지막 1을 뚫기 위해 앞에있는 1을 피해서 가는 경우를 탐색할 줄 모름.


n, m = map(int, input().split())
maps = []

for _ in range(n):
    temp = list(map(int, list(input())))
    maps.append(temp)

visited = [[[False, False] for i in range(m)] for i in range(n)]
# visited의 각 요소가 [False, False]인 것은 우리가 각 방을 지나면서 벽을 부수면서 왔는지 아닌지 기록하기 위함임.
# 0,0에서 0,1 로 갈때 벽을 부수면서 진행할땐 wall변수가 0이라서 0, 0도 0, 1도 [True, False] 임.
# 이때 0, 1부분을 큐에서 꺼내면 wall변수가 1이 돼버렸으므로 [True, True]가 되고, 방금 지나온 0, 1은 아직 visited의 두번째 요소가 False이므로 다시 지나오게됨.
# 0이 아니라 1을 통해서 온 친구는 계속해서 visited의 1번 인덱스만 True로 만들어주기 때문에 방을 이동할때 visited의 0번 인덱스를 체크하는 아직 벽을 뚫고 오지 않은 친구가 올 수 있음.
# 그 중에서도 가장 짧은 거리를 이동한 친구만을 뽑기 위해 heap을 사용한다.


def bfs1():
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = []
    heapq.heappush(q, (1, 0, 0, 0))
    while q:
        cnt, wall, y, x = heapq.heappop(q)
        visited[y][x][wall] = True
        if y == n-1 and x == m-1:
            return cnt
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx][wall]:
                if maps[ny][nx] == 0 or (maps[ny][nx] == 1 and wall == 0):
                    visited[ny][nx][wall] = True
                    if maps[ny][nx] == 0:
                        heapq.heappush(q, [cnt+1, wall, ny, nx])
                    else:
                        heapq.heappush(q, [cnt+1, wall + 1, ny, nx])
    return -1


print(bfs1())
# heapq를 사용해서 다시 풀어볼것
