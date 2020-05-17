n, s, m = map(int, input().split())

dp = [[False for i in range(m + 1)] for i in range(n + 1)]
songs = [0] + list(map(int, input().split()))
dp[0][s] = True

for i in range(1, len(dp)):
    for j in range(m+1):
        if dp[i-1][j]:
            plus, minus = j + songs[i], j - songs[i]
            if plus <= m:
                dp[i][plus] = True
            if minus >= 0:
                dp[i][minus] = True

for i in range(len(dp[-1])-1, -1, -1):
    if dp[-1][i]:
        print(i)
        break
else:
    print(-1)

# dp에서 가장 중요한건 메모이제이션을 할 배열을 만드는것. 여기선 재생 가능한 볼륨을 idx로 하는 배열로 메모이제이션을 했다.
# 주어진 변수 들을 활용해 이런 저런 메모이제이션 틀을 만들어 봄으로써 문제를 풀어 나갈 수 있다.
