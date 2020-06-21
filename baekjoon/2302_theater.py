n = int(input())

vip = []
for i in range(int(input())):
    vip.append(int(input()))

dp = [0 for i in range(n+1)]
dp[0], dp[1] = 1, 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

if vip:
    vip.sort()
    result = 1
    for i in range(1, len(vip)):
        result *= dp[vip[i] - vip[i-1] - 1]
    if vip[0] != 1:
        result *= dp[vip[0]-1]
    if vip[-1] != n:
        result *= dp[n - vip[-1]]

    print(result)
else:
    print(dp[n])

# 피보나치 + 고정된 좌석을 경계로 다른 부분을 쪼개고 각 쪼개진 부분의 좌석수를 피보나치에서 끌어와서 곱하면 경우의수 도출 가능
