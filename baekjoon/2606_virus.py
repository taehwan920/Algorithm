com = int(input())
con = int(input())
net = [0] * (com + 1)
visited = [-1] + [False] * com
for i in range(con):
    a, b = map(int, input().split())
    if net[a] == 0:
        net[a] = [b]
    else:
        net[a].append(b)
    if net[b] == 0:
        net[b] = [a]
    else:
        net[b].append(a)


def bfs(num):
    q = [num]
    visited[num] = True
    count = -1
    while q:
        temp = q.pop(0)
        count += 1
        for i in net[temp]:
            if not(visited[i]):
                visited[i] = True
                q.append(i)
    return count


def dfs(num):
    visited[num] = True
    for i in net[num]:
        if not(visited[i]):
            dfs(i)


# print(bfs(1))
# dfs(1)
print(visited.count(True) - 1)

# dfs, bfs 두 알고리즘 다 정답을 찾을 수 있는 문제라 연습 겸 둘 다 써봤다.
