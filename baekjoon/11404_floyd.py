import heapq
import sys
input = sys.stdin.readline

cities = int(input())
bus = int(input())

graph = [[] for i in range(cities + 1)]
for i in range(bus):
    s, e, w = map(int, input().split())
    graph[s].append([w, e])

result = []


def dijk(start):
    q = [[0, start]]
    distance = [1e9 for i in range(cities + 1)]
    distance[start] = 0
    while q:
        c, now = heapq.heappop(q)
        for w, node in graph[now]:
            cost = w + c
            if distance[node] <= cost:
                continue
            distance[node] = cost
            heapq.heappush(q, [cost, node])

    distance = list(map(lambda x: 0 if x == 1e9 else x, distance))
    result.append(distance[1:])


for i in range(1, cities + 1):
    dijk(i)

for i in range(len(result)):
    for j in range(len(result[0])):
        print(result[i][j], end=" ")
    print()
