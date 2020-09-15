import heapq
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[] for i in range(n+1)]

for i in range(r):
    a, b, l = map(int, input().split())
    graph[a].append([l, b])
    graph[b].append([l, a])

distances = [[]]


def dijk(start):
    q = [[0, start]]
    distance = [1e9 for i in range(n+1)]
    distance[start] = 0
    while q:
        now_l, now = heapq.heappop(q)
        for new_l, new in graph[now]:
            cost = new_l + now_l
            if distance[new] <= cost:
                continue
            distance[new] = cost
            heapq.heappush(q, [cost, new])
    distances.append(distance)


result = 0

for i in range(1, n+1):
    dijk(i)
    temp = 0
    search_spot = distances[i]
    for j in range(1, n+1):
        if search_spot[j] <= m:
            temp += items[j]
    result = temp if temp > result else result

print(result)
