class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 1:
            return 0
        if n < 3:
            return max(nums)

        dp1 = [0] * n
        dp2 = [0] * n
        dp1[1] = nums[1]
        dp2[0] = nums[0]
        dp2[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp1[i] = max(dp1[i-1], nums[i] + dp1[i-2])
            if i == n - 1:
                dp2[i] = 0
            else:
                dp2[i] = max(dp2[i-1], nums[i] + dp2[i-2])

        return max(max(dp1), max(dp2))
