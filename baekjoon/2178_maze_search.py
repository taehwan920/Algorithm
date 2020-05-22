from collections import deque
import sys
ipt = sys.stdin.readline
n, m = map(int, ipt().split())
maze = []
for i in range(n):
    maze.append(list(map(int, list(input()))))

visited = [[False for i in range(m)] for i in range(n)]
step = 1


def bfs(y, x, num):
    q = deque([[y, x, num]])
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited[y][x] = True
    while q:
        temp = q.popleft()
        ty, tx = temp[0], temp[1]
        tnum = temp[2]
        if ty == n-1 and tx == m-1:  # queue를 pop했다는 것 == 해당 블럭에 도착했다는것 => 그러므로 도착지에 도달했을 때 return을 한다. 방의 갯수는 queue에 넣을때 이미 합산 되어있으므로 건들 필요 x
            return tnum
        for dy, dx in direction:
            ny, nx = ty + dy, tx + dx
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if maze[ny][nx] and not visited[ny][nx]:
                # 다음에 이동해야하는 방이므로 방문한 방 개수를 하나 늘려서 좌표와 함께 배열에 넣어준다.
                new_num = tnum + 1
                # bfs는 해당 방을 q에 넣을때 방문 처리하는 것 / 반복문 돌기 전에 방문처리 하는 두가지 경우가 있음.
                visited[ny][nx] = True
                q.append([ny, nx, new_num])


print(bfs(0, 0, step))
