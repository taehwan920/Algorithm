import heapq

t = int(input())

direction = [(-1, -2), (-2, -1), (-2, 1), (-1, 2),
             (1, 2), (2, 1), (2, -1), (1, -2)]


def bfs(n, target, start):
    q = []
    heapq.heappush(q, [0, start[0], start[1]])
    board[start[0]][start[1]] = 1
    while q:
        cnt, y, x = heapq.heappop(q)
        if target == [y, x]:
            return cnt
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
                heapq.heappush(q, [cnt + 1, ny, nx])
                board[ny][nx] = 1


for lt in range(t):
    n = int(input())
    start = list(map(int, input().split()))
    target = list(map(int, input().split()))
    board = [[0 for j in range(n)] for i in range(n)]
    print(bfs(n, target, start))

# 문제자체는 그리 안어려웠는데 direction 배열 부분에 오타가 있어 계속 틀린 문제였다. 오타 체크 꼼꼼히 할 것..
