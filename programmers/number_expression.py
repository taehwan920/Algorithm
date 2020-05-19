def solution(n):
    dp = [i for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(i + 1, n+1):
            if dp[i] < n:
                dp[i] += j
            else:
                break
    return dp.count(n)

# n보다 작거나 같은 모든 자연수에서 시작하는 경우의수를 체크.
# 각 자연수들을 그 다음 수와 계속 더하면서, n보다 크거나 같아지면 더이상 더하지 않고 내버려 둔다.
# 연산이 끝나면 dp에서 n이 몇개있는지 찾으면 연속된 자연수를 더하여 n이 나오는 경우의 수를 구할 수 있다.
