import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [False for i in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

connected = 0


def bfs(num):
    q = [num]
    while q:
        temp = q.pop(0)
        if not visited[temp]:
            visited[temp] = True
            for i in graph[temp]:
                q.append(i)


def dfs(num):
    visited[num] = True
    for i in graph[num]:
        if not visited[i]:
            dfs(i)


for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        connected += 1

print(connected)
# 반복문으로 탐색하기 때문에 bfs는 시간초과가 떴다. 그래서 dfs로 풀이했다.
