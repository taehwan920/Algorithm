class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            temp = nums[i] + dp[i-1]
            if temp < nums[i]:
                dp[i] = nums[i]
            else:
                dp[i] = temp
        return max(dp)
