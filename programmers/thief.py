def solution(money):
    n = len(money)
    dp1 = [0] * n
    dp2 = [0] * n
    dp1[0] = 0
    dp1[1] = money[1]
    dp2[0] = money[0]
    dp2[1] = max(money[0], money[1])

    for i in range(2, n):
        if i == n - 1:
            dp1[n-1] = max(dp1[i-1], money[i] + dp1[i-2])
            dp2[n-1] = 0
        else:
            dp1[i] = max(dp1[i-1], money[i] + dp1[i-2])
            dp2[i] = max(dp2[i-1], money[i] + dp2[i-2])
    return max(max(dp1), max(dp2))
# 조건이 공존이 안되는 경우는 두가지로 쪼개서 메모이제이션..
