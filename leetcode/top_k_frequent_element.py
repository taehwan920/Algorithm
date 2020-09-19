import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kinds = list(set(nums))
        sample = []
        for kind in kinds:
            heapq.heappush(sample, [-nums.count(kind), kind])

        result = []
        for i in range(k):
            result.append(heapq.heappop(sample)[1])
            if i == k - 1:
                break

        return result
