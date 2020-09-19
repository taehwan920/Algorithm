import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -x, stones))
        heapq.heapify(stones)

        while len(stones) >= 2:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)

            if a != b:
                heapq.heappush(stones, -abs(a - b))

        return -stones[0] if stones else 0
