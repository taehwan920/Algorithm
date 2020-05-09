from collections import deque

n, m, v = map(int, input().split())

graph = [[]for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for e in graph:
    e.sort()


def dfs(v):
    print(v, end=" ")
    visited[v] = True
    for e in graph[v]:
        if not(visited[e]):
            dfs(e)


def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if not(visited[v]):
            visited[v] = True
            print(v, end=" ")
            for e in graph[v]:
                if not visited[e]:
                    q.append(e)


visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)
