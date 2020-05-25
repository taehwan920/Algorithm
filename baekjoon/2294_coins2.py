import sys
n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
dp = [0 for i in range(k+1)]
for i in range(1, k+1):
    temp = []
    for j in coins:
        if i >= j and dp[i-j] != -1:
            temp.append(dp[i-j])
    if temp:
        dp[i] = min(temp) + 1
    else:
        dp[i] = -1

print(dp[k])

# 역시 처음 생각했던대로 각 동전 별로 쓰이는 개수를 파악해서 그중 최소값을 메모이제이션 하는 방식으로 풀 수 있다.
