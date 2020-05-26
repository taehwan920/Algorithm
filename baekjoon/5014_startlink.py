from collections import deque
f, s, g, u, d = map(int, input().split())
d *= -1
visited = [False for i in range(f+1)]


def bfs():
    q = deque([[0, s]])
    while q:
        cnt, now = q.popleft()
        visited[now] = True
        if now == g:
            return cnt
        for i in (u, d):
            move = now + i
            if 0 < move <= f:
                if not visited[move]:
                    visited[move] = True
                    q.append([cnt + 1, move])
    return -1


result = bfs()
print(result) if result != -1 else print('use the stairs')

# 가장 낮은 층이 0층이 아니라 1층인데 move의 범위설정을 잘못해서 두번틀림.
