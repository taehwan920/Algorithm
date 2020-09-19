import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        for row in matrix:
            arr.extend(row)

        heapq.heapify(arr)

        result = 0
        for i in range(k):
            result = heapq.heappop(arr)

        return result
