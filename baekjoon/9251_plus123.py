t = int(input())

for _ in range(t):
    n = int(input())
    memo = [0] * (n+1)
    for i in range(1, n+1):
        if i == 1:
            memo[1] = 1
        elif i == 2:
            memo[2] = 2
        elif i == 3:
            memo[3] = 4
        else:
            memo[i] = sum(memo[i-3:i])
    print(memo[-1])
# 항간 차이만 구하려고 하지 말고 수열 그자체를 잘 관찰해 보는것도 좋음.
