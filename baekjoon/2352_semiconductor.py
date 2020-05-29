n = int(input())
elec = list(map(int, input().split()))
dp = [1 for i in range(n)]

for i in range(1, n):
    for j in range(i):
        if elec[j] < elec[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))

# LIS 응용문제.
