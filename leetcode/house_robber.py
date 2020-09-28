class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 1:
            return 0
        dp = [0 for i in range(n)]

        for i in range(n):
            dp[i] = nums[i]
            if i == 2:
                dp[i] += dp[i-2]
            if i > 2:
                dp[i] += max(dp[i-2], dp[i-3])

        return max(dp)

# 테스트 케이스 두 개 맞았다고 다 맞은게 아니었음
# 조건을 역시 잘 읽어보고 차근차근 경우의 수를 생각해봐야함..
