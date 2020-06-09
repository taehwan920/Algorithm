def solution(n):
    dp1, dp2 = 1, 1
    for i in range(1, n):
        dp1, dp2 = dp2, dp1 + dp2
    return dp2 % 1234567
