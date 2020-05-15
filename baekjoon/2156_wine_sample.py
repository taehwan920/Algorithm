n = int(input())

wine = [0]
dp = [0] * (n+1)

for i in range(n):
    wine.append(int(input()))

for i in range(1, n+1):
    if i == 1:
        dp[1] = wine[1]
    elif i == 2:
        dp[2] = wine[2] + wine[1]
    else:
        dp[i] = max(wine[i] + dp[i-2], wine[i] + wine[i-1] + dp[i-3], dp[i-1])

print(dp[n])
# n과 인덱스를 맞춰서 설계할 것
# 문제를 잘 읽어보고, 경우의수를 잘 파악할 것. 계단 문제와 달리 포도주는 해당 와인을 선택하지 않는다는 선택지도 있었음.
