n = int(input())

board = [[] for i in range(n)]
visited = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    temp = list(map(int, input().split(' ')))
    for idx, num in enumerate(temp):
        if num:
            board[i].append(idx)


def dfs(node):
    stack = [node]
    while stack:
        now = stack.pop()
        for new in board[now]:
            if visited[node][new]:
                continue
            stack.append(new)
            visited[node][new] = 1


for i in range(n):
    dfs(i)

for result in visited:
    print(' '.join(list(map(str, result))))
