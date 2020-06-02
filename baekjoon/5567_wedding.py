from collections import deque

n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
visited = [False for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

invite = -1
q = deque([[0, 1]])
visited[1] = True
while q:
    cnt, node = q.popleft()
    if cnt <= 2:
        invite += 1
    for i in graph[node]:
        if not visited[i]:
            visited[i] = True
            q.append([cnt + 1, i])

print(invite)
