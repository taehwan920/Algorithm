from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    temp = list(map(int, input().split()))
    perms = [0] + temp
    cnt = 0
    visited = [0 for i in range(n + 1)]

    def bfs(start):
        q = deque([start])
        while q:
            now = q.popleft()
            if visited[now] == 1:
                continue
            q.append(perms[now])
            visited[now] = 1
        return 1

    for i in range(1, n+1):
        if visited[i] == 1:
            continue
        cnt += bfs(i)

    print(cnt)
