import heapq

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
distance = [1e9 for i in range(n+1)]

for i in range(m):
    s, e, w = map(int, input().split())
    graph[s].append([w, e])


def dijk(start):
    q = []
    heapq.heappush(q, [0, start])
    while q:
        weight, now = heapq.heappop(q)
        for n_weight, next_node in graph[now]:
            cost = weight + n_weight
            if cost >= distance[next_node]:
                continue
            distance[next_node] = cost
            heapq.heappush(q, [cost, next_node])


start, end = map(int, input().split())
dijk(start)
print(distance[end])
