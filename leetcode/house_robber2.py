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

# dp1은 nums[0]을 계산에 넣지 않은 채로 계산한 값을 기록한 배열
# dp2는 nums[n-1]을 계산에 넣지 않은 채로 계산한 값을 기록한 배열
# 배열의 양 끝 값은 서로 인접한 상태로 판정되므로 각 값을 포함하지 않고 계산한 경우를 따로따로 기록하여 두 배열의 최대값 중 더 큰 값이 답이 됨.
