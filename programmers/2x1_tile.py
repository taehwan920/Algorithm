def solution(n):
    if n == 1:
        return 1
    dp = [0, 1, 2]
    for i in range(2, n):
        dp[0], dp[1], dp[2] = dp[1], dp[2], dp[1] + dp[2]
    return dp[-1] % 1000000007
