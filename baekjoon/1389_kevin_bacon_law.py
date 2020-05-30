import heapq

n, m = map(int, input().split())
friends = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)


def bfs(num):
    visited = [0 for i in range(n+1)]
    q = []
    heapq.heappush(q, [0, num])
    visited[num] = 0
    while q:
        cnt, fri = heapq.heappop(q)
        for i in friends[fri]:
            if visited[i] == 0:
                heapq.heappush(q, [cnt+1, i])
                visited[i] = cnt+1
    return sum(visited)


result = [0]
for i in range(1, n+1):
    result.append(bfs(i))
print(result.index(min(result[1:])))

# 반복문 범위 설정 변수에 n을 넣어야하는데 m을 넣어서 자꾸 틀렸다. 변수 입력에 주의.
