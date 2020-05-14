n = int(input())

dp = [0] * (n + 1)
nums = [0] + list(map(int, input().split()))

for i in range(1, n+1):
    accum = nums[i] + dp[i-1]
    if nums[i] < accum:
        dp[i] = accum
    else:
        dp[i] = nums[i]
dp.pop(0)

print(max(dp))
