n, m = map(int, input().split())

dp1 = list(map(int, input().split()))
for i in range(1, m):
    dp1[i] = dp1[i-1] + dp1[i]

dp2 = [0 for i in range(m)]
for i in range(n-1):
    temp = list(map(int, input().split()))
    for j in range(m):
        if j == 0:
            dp2[j] = dp1[j] + temp[j]
        else:
            dp2[j] = max(dp2[j-1] + temp[j], dp1[j-1] +
                         temp[j], dp1[j] + temp[j])
    dp1 = dp2[:]

print(max(dp1))

# 슬라이딩 윈도우 알고리즘
