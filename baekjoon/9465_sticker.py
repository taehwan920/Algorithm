t = int(input())
for _ in range(t):
    n = int(input())
    dp = [list(map(int, input().split())), list(map(int, input().split()))]
    if n == 1:
        print(max(dp[0], dp[1]))
        continue
    dp[0][1], dp[1][1] = dp[1][0] + dp[0][1], dp[0][0] + dp[1][1]
    for i in range(2, n):
        dp[0][i] += max(dp[0][i-2], dp[1][i-2], dp[1][i-1])
        dp[1][i] += max(dp[0][i-2], dp[1][i-2], dp[0][i-1])
    print(max(max(dp[0]), max(dp[1])))

# 전전열의 두 행, 전 열의 나와 다른 행의 값들 중 최대 값을 현재 스티커값에 계속 더해주면서
