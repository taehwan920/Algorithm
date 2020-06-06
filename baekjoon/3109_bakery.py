def dfs(y, x):
    if x == c - 1:
        return True
    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if 0 <= ny < r and board[ny][nx] == '.' and not visited[ny][nx]:
            visited[ny][nx] = True
            if dfs(ny, nx):
                return True
    return False


r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
direction = [(-1, 1), (0, 1), (1, 1)]


class pipe:
    cnt = 0


for i in range(r):
    if board[i][0] == '.':
        if dfs(i, 0):
            pipe.cnt += 1

print(pipe.cnt)

# dfs 응용문제인데 계속해서 틀렸다고 나와서 이상했는데 이유를 찾아냈다.
# 1. dfs도 bfs처럼 넣을때 visited처리를 해줘야하는 문제가 있었는데 이게 그 유형.
# 2. 찾는 순서도 위에서부터 아래로 차근차근 찾았어야했음. direction 배열의 순서를 바꿨다가 혹시 이게 문제인가 싶어 순서를 위 -> 아래 방향으로 정렬해주었더니 정답이 나왔다.
# 3. 재귀 넣을때 visited 처리를 해주는게 백트래킹..?일지도
