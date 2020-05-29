n = int(input())
elec = []
for i in range(n):
    elec.append(list(map(int, input().split())))
elec.sort()
dp = [1 for i in range(n)]
for i in range(1, n):
    for j in range(i):
        if elec[j][1] < elec[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))

# 이게 왜 LIS냐 하면 전깃줄이 겹치지 않도록 최소 개수의 전깃줄을 제거한다는 소리는 즉 전깃줄이 겹치지 않는 최대 전깃줄 갯수를 구해 총 전봇대 개수에서 빼면 됨.
# 연결이 시작되는 전봇대 순으로 정렬한 뒤, 연결을 해야하는 전봇대의 번호가 증가하는 부분수열로 이루어져 있어야 겹치지 않음. 그래서 그중 가장 긴 수열을 골라서 총 전봇대 개수에서 빼면 됨.
# 그래서 LIS 응용문제.
