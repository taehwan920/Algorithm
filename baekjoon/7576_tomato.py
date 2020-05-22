from collections import deque

m, n = map(int, input().split())
tomatoes = []
q = deque([])
visited = [[False for i in range(m)] for i in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] == 1:
            q.append(([i, j, 0]))
            visited[i][j] = True
# 시작점이 따로 주어지지 않음 -> 익은 토마토의 초기 개수를 알수가 없으므로 초기 배열 안의 모든 익은 토마토를 queue에 넣어준 뒤 bfs로 토마토 숙성을 진행.
    tomatoes.append(temp)

result = []
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while q:
    ty, tx, tnum = q.popleft()
    result.append(tnum)
    tomatoes[ty][tx] = 1  # pop되는 시점이 토마토가 익는 시점이므로 1로 만들어줄 것.
    for dy, dx in direction:
        ny, nx = ty + dy, tx + dx
        if ny < 0 or ny >= n or nx < 0 or nx >= m or tomatoes[ny][nx] == -1:
            continue
        if tomatoes[ny][nx] == 0 and not visited[ny][nx]:
            # 다음 토마토를 pop할 땐 하루가 지나있으므로 tnum에 1을 더해서 배열에 저장
            q.append([ny, nx, tnum+1])
            visited[ny][nx] = True

# 탐색이 끝난 뒤에도 안 익은 토마토가 있는지 검사
for i in range(n):
    if 0 in tomatoes[i]:
        print(-1)
        break
else:
    print(max(result))
