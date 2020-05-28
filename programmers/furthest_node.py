import heapq


def solution(n, edge):
    graph = [[] for i in range(n + 1)]
    visited = [-1] * (n + 1)
    for node in edge:
        graph[node[0]].append(node[1])
        graph[node[1]].append(node[0])

    def bfs(arr):
        q = []
        heapq.heappush(q, arr)
        while q:
            cnt, node = heapq.heappop(q)
            if visited[node] == -1:
                visited[node] = cnt
                for i in graph[node]:
                    if visited[i] == -1:
                        heapq.heappush(q, [cnt + 1, i])
    bfs([0, 1])
    return visited.count(max(visited))
# 지나온 간선 개수를 굳이 따로 배열을 만들지 말고 visited에 저장하면 메모리를 덜 먹을 수 있음
