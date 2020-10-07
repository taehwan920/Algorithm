class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    result += 1

        return result
