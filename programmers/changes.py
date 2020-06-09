def solution(n, money):
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    money.sort()
    for coin in money:
        for i in range(1, n+1):
            if i >= coin:
                dp[i] = dp[i] + dp[i-coin]
    return dp[-1] % 1000000007
