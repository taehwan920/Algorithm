# Longest Bitonic Subsequence

n = int(input())

nums = list(map(int, input().split()))

dp1 = [1 for i in range(n)]
for i in range(1, n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

dp2 = [1 for i in range(n)]
nums.reverse()
for i in range(1, n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
dp2.reverse()

for i in range(n):
    dp1[i] += dp2[i]
    dp1[i] -= 1

print(max(dp1))

# 주어진 배열의 각 요소 별로 LIS, LDS를 구한 뒤 둘을 합쳐서 1을 빼면 바이토닉 수열을 구할 수 있다.
# nums의 각 요소는 LIS를 구할 때 한번, LDS를 구할 때 한번 셌기 때문에 두 경우의 수를 합친 뒤 1을 빼야 중복 카운팅을 배제할 수 있기 때문에 1을 뺐다.
