n = int(input())
board = []
dp = [[0] * n for i in range(n)]
dp[0][0] = 1
for i in range(n):
    board.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            break
        if dp[i][j] == 0:
            continue
        temp_i, temp_j = board[i][j] + i, board[i][j] + j
        if temp_i < n:
            dp[temp_i][j] += dp[i][j]
        if temp_j < n:
            dp[i][temp_j] += dp[i][j]

print(dp[-1][-1])


# 현재 칸에서 갈 수 있는 부분만 가짓수에 더해주면 된다.
# dp로 board의 각 칸에서 갈 수 있는 경우의 수를 다 저장해주는데, 첫칸의 경우의수는 무조건 1이고, 각 칸에서 갈 수 있는 칸에는 현재 칸까지 올 수 있는 경우의 수를 더해주면 된다.
# 첫 칸을 통해서 갈 수 없는 모든 칸들은 절대 갈 수 없으므로 dp[i][j]가 0인 곳은 다 무시해주면된다.
