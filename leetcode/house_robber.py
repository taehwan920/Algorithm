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


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 1:
            return 0
        if n < 3:
            return max(nums)
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return max(dp)

# 다른 풀이.
# dp는 각 단계에서 최대값(혹은 최소값)을 저장하는 배열일 뿐이기 때문에, 간격을 두고 값을 계산해야하는 경우 그냥 바로 전의 값과 그 전전 값을 비교해주는 식으로 최대값을 계속 기록하면 됨.
