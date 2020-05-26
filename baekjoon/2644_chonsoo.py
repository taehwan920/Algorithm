import heapq

n = int(input())
me, him = map(int, input().split())
network = [[] for i in range(n+1)]
visited = [False for i in range(n+1)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    network[x].append(y)
    network[y].append(x)


def bfs():
    q = []
    heapq.heappush(q, [0, me])
    while q:
        cnt, guy = heapq.heappop(q)
        visited[guy] = True
        if guy == him:
            return cnt
        for i in network[guy]:
            if not visited[i]:
                visited[i] = True
                heapq.heappush(q, [cnt+1, i])
    return -1


print(bfs())
