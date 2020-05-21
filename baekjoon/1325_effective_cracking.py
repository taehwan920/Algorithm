from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
coms = [[] for i in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    coms[b].append(a)


def bfs(num):
    q = deque([num])
    visited = [False] * (n+1)
    visited[num] = True
    count = 1
    while q:
        temp = q.popleft()
        for i in coms[temp]:
            if not visited[i]:
                q.append(i)
                visited[temp] = True
                count += 1
    return count


result = []
max_value = -1

for i in range(1, n+1):
    c = bfs(i)
    if c > max_value:
        result = [i]
        max_value = c
    elif c == max_value:
        result.append(i)
        max_value = c

for e in result:
    print(e, end=" ")

# 로직은 이게 맞는데 몇번을 시도해도 시간초과가 떠서 정답을 낼수가 없었다.
