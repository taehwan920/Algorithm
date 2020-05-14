t = int(input())

for _ in range(t):
    dp = [1, 1, 1, 2, 2]
    n = int(input())
    if n <= 5:
        print(dp[n-1])
        continue
    for i in range(5, n):
        temp = dp[i-1] + dp[i-5]
        dp.append(temp)
    print(dp[-1])
