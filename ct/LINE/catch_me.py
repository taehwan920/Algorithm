import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    c, b = map(int, input().split())
    MAX = 200001
    visited = [False for i in range(MAX)]
    c_move = 0
    q = deque([[b, 0]])
    visited[b] = True
    while q:
        now_b, time = q.popleft()
        if now_b == c:
            return time
        for i in (now_b - 1, now_b + 1, now_b * 2):
            if not visited[i] and 0 <= i < MAX:
                q.append([i, time + 1])
        if len(list(filter(lambda x: x[1] == c_move, q))) == 0:
            c_move += 1
            c += c_move
            if c > MAX:
                break
    return -1


print(bfs())
