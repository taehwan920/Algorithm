import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda x: -x, nums))
        heapq.heapify(nums)
        result = 0
        for i in range(k):
            if i == k - 1:
                result = heapq.heappop(nums)
                break
            heapq.heappop(nums)

        return -result
