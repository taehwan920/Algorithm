n = int(input())

if n == 0:
    print(0)
    exit(0)

dp = [[1] * 10 for i in range(n)]

for i in range(1, n):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[-1][1:]) % 1000000000)
