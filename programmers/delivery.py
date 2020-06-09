import heapq


def solution(n, road, k):
    distance = [1e9] * (n + 1)
    city = [[] for i in range(n + 1)]
    for route in road:
        city[route[0]].append([route[2], route[1]])
        city[route[1]].append([route[2], route[0]])
    q = []
    heapq.heappush(q, [0, 1])
    distance[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in city[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, [cost, i[1]])
    return len(list(filter(lambda x: x <= k, distance)))

# 평범한 다익스트라 알고리즘 문제.
