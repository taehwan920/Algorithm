def solution(m, n, puddles):
    routes = []
    for i in range(n):
        temp = []
        for j in range(m):
            if [j+1, i+1] in puddles:
                temp.append(0)
            else:
                if i == 0 and j == 0:
                    temp.append(1)
                if i != 0 and j != 0:
                    ways = routes[i - 1][j] + temp[j-1]
                    temp.append(ways)
                if i == 0 and j != 0:
                    if temp[j-1] != 0:
                        temp.append(1)
                    else:
                        temp.append(0)
                if i != 0 and j == 0:
                    if routes[i-1][0] != 0:
                        temp.append(1)
                    else:
                        temp.append(0)
        routes.append(temp)

    return routes[-1][-1] % 1000000007
# 동적계획법의 과정중에 완전탐색이 있을 뿐


def solution1(m, n, puddles):
    dp = [[1 for j in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            if [j+1, i+1] in puddles:
                if i == 0:
                    for k in range(j, m):
                        dp[i][k] = 0
                elif j == 0:
                    for k in range(i, n):
                        dp[k][j] = 0
                else:
                    dp[i][j] = 0
                continue
            if i == 0 or j == 0:
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1] % 1000000007

# 전에 풀었던 건 거의 단순 구현 식이라 이번엔 좀 더 dp스럽게 풀어보았다.
