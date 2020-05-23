def solution(n, computers):
    visited = [False for i in range(n)]
    coms = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                if computers[i][j] == 1:
                    coms[i].append(j)

    def dfs(num):
        visited[num] = True
        for i in coms[num]:
            if not visited[i]:
                dfs(i)
    network = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            network += 1
    return network
