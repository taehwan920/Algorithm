n = int(input())

dp = [0] * (n + 1)

dis1 = 4
dis2 = 8
for i in range(1, n+1):
    if i == 1:
        dp[1] = 1
    elif i == 2:
        dp[2] = 3
    elif i % 2 != 0:
        dp[i] = dp[i-2] + dis1
        dis1 *= 4
    else:
        dp[i] = dp[i-2] + dis2
        dis2 *= 4

print(dp[-1] % 10007)
