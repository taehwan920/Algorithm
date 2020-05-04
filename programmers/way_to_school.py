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
