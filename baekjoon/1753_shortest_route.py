import heapq
import sys
input = sys.stdin.readline


def djikstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    # heap에 넣는 튜플은 (가중치, 노드 번호)
    distance[start] = 0
    # 첫 노드는 가중치랄게 없으니 0으로 처리.
    while heap:
        dist, now = heapq.heappop(heap)
        # heap의 가장 앞에있는 데이터의 가중치와 노드 번호.
        if distance[now] < dist:
            # 이미 기록된 가중치보다 새로 꺼낸 가중치가 더 크면 무시.
            continue
        for i in nodes[now]:
            # 새로 꺼낸 가중치가 더 작다면 해당 노드와 연결된 모든 노드들을 확인.
            cost = dist + i[1]
            # 연결된 각 노드들의 가중치를 합산. 나중에 풀이할때는 가중치/노드번호 위치를 통일 시키자.
            if cost < distance[i[0]]:
                # 만약 누산된 가중치가 이미 기록된 가중치보다 작다면 갱신.
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))
                # 누산된 가중치가 더 작아서 이쪽 루트를 통해서 가게 될 것이므로 누산치가 기존 기록치보다 작을때만 힙큐에 데이터를 추가.


v, e = map(int, input().split())
start = int(input())
nodes = [[] for i in range(v+1)]
distance = [1e9] * (v+1)  # 가지 않는 루트의 가중치는 무조건 무한대로 잡고함.
for _ in range(e):
    u, v, w = map(int, input().split())
    nodes[u].append((v, w))
djikstra(start)
distance.pop(0)
for i in distance:
    if i == 1e9:
        print("INF")
    else:
        print(i)

# 기본 다익스트라 알고리즘 풀이.
