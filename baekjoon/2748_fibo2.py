n = int(input())

dp = [0, 1]

if n == 0:
    print(dp[0])
    exit(0)
if n == 1:
    print(dp[1])
    exit(0)

for i in range(2, n+1):
    temp = dp[0] + dp[1]
    dp[0], dp[1] = dp[1], temp

print(dp[-1])
