import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = [[] for i in range(N + 1)]
        for u, v, w in times:
            graph[u].append([w, v])

        def djik(start):
            q = [[0, start]]
            distance = [1e9 for i in range(N+1)]
            distance[start] = 0
            while q:
                w, v = heapq.heappop(q)
                for n_w, n_v in graph[v]:
                    cost = n_w + w
                    if cost >= distance[n_v]:
                        continue
                    distance[n_v] = cost
                    heapq.heappush(q, [cost, n_v])
            return distance

        n_dist = djik(K)[1:]
        return -1 if 1e9 in n_dist else max(n_dist)
