import heapq

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [False for i in range(n+1)]
result = [n+1 for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = []
heapq.heappush(q, [0, 1])
visited[1] = True
while q:
    dist, node = heapq.heappop(q)
    result[node] = min(result[node], dist)
    for i in graph[node]:
        if not visited[i]:
            heapq.heappush(q, [dist+1, i])
            visited[i] = True

result[0] = -1
nominee = max(result)
print(result.index(nominee), nominee, result.count(nominee))

# 제대로 정답을 출력하는데에 방해가 되는 result[0]을 연산이 다 끝난 뒤 -1 과같이 정답과 전혀 상관없는 값으로 변경해 주어 정답을 낼 수 있도록 한다.
