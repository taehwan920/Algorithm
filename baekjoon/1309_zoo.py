n = int(input())
dp = [1, 3]

for i in range(2, n+1):
    dp[1], dp[0] = (2 * dp[1]) + dp[0], dp[1]
print(dp[-1] % 9901)

# dp의 핵심
# 1. 메모이제이션
# 2. 온갖 수를 다 동원해서라도 수열의 규칙을 찾아내야함.
