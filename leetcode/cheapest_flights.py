import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = [[] for i in range(n)]
        for s, e, w in flights:
            graph[s].append([w, e])

        def dijk(start):
            q = [[0, 0, start]]
            distance = [1e9 for i in range(n)]
            distance[start] = 0
            while q:
                step, dist, node = heapq.heappop(q)

                for new_d, new_n in graph[node]:
                    if step > K:
                        continue
                    cost = dist + new_d
                    if cost >= distance[new_n]:
                        continue
                    distance[new_n] = cost
                    heapq.heappush(q, [step + 1, cost, new_n])

            return distance

        calc1 = dijk(src)

        calc2 = calc1[dst]

        return -1 if calc2 == 1e9 else calc2
