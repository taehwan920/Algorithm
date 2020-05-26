import heapq

n, m, x = map(int, input().split())
graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((w, b))


def djikstra(start, end):
    temp_dist = [1e9 for i in range(n+1)]
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if temp_dist[now] < dist:
            continue
        for i in graph[now]:
            cost = i[0] + dist
            if temp_dist[i[1]] > cost:
                temp_dist[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))
    return temp_dist[end] if temp_dist[end] != 1e9 else 0


result = [0 for i in range(n+1)]
for i in range(n+1):
    if i != x:
        result[i] = djikstra(i, x)
        result[i] += djikstra(x, i)

print(max(result))
# 단방향 그래프 왕복문제이기 때문에 시작점과 끝점을 바꾸어 다익스트라 연산을 두번해서 가는 길을 구했다.
