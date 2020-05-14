n = int(input())

dp = [0] * n
stair = []

for i in range(n):
    stair.append(int(input()))

for i in range(n):
    if i == 0:
        dp[0] = stair[0]
    elif i == 1:
        dp[1] = stair[1] + dp[0]
    elif i == 2:
        dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
        # 여기부터 선택지. 첫번째 계단 밟은 경우/안밟은 경우 중 더 큰값
    else:
        dp[i] = max(stair[i] + stair[i-1] + dp[i-3], stair[i] + dp[i-2])
        # 1. 전전 계단(누적값)을 밟고 nth계단을 밟는 경우
        # 2. 전계단(누적값아님)+전전전계단(누적값) 중 선택
        # 1의 경우 세번연속 밟은게 아니라는게 확실해서 누적값을 가져와서 더함.
        # 2의 경우 전계단을 누적값을 가져와 버리면 이게 세번연속밟는건지 판단이 불가능해서 이와같이계산

print(dp[-1])
