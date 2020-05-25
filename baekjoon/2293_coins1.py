import sys
n, k = map(int, sys.stdin.readline().split())
dp = [0 for i in range(k+1)]
dp[0] = 1
coins = []
for _ in range(n):
    coins.append(int(input()))
for i in coins:
    for j in range(1, k+1):
        if j >= i:
            dp[j] += dp[j-i]

print(dp[-1])

# 그리디의 거스름돈 + dp의 배낭 문제와 굉장히 유사한 문제였음.
# 목표한 돈 k 까지 가는 와중의 경우의 수를 전부 메모이제이션함.
# k까지 가는 도중의 숫자들과 각 동전의 크기를 비교해서 동전의 크기보다 크거나 같은 모든 수는 해당 수에서 동전의 크기만큼을 뺀 수의 경우의 수를 다시 더해줌.
# 예를 들어 4는 4에서 1을 뺀 결과인 3의 경우의수인 2를 dp[4]에 더해주고, 4에서 2를 뺀 결과인 2의 경우의수인 2도 dp[4]에 더해줌으로써 타겟이 4일 경우 경우의 수가 4인 걸 알아낼 수 있다.
# 5는 4보다 크므로 계산하지않는다.
