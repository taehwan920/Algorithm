from collections import deque


def solution(board):
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    n = len(board)
    costs = [[1e9 for i in range(n)] for i in range(n)]
    costs[0][0] = 0
    q = [[0, 0, 0, 0, 0]]

    result = 1e9
    q = deque([[0, 0, 0, 0, 0]])
    while q:
        cost, y, x, prev_y, prev_x = q.popleft()
        if y == x == n-1:
            result = min(result, cost)
            continue
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            new_cost = cost + 600 if ny != prev_y and nx != prev_x else cost + 100
            if board[ny][nx] or new_cost > costs[ny][nx]:
                continue
            costs[ny][nx] = new_cost
            if cost:
                q.append([new_cost, ny, nx, y, x])
            else:
                q.append([cost + 100, ny, nx, 0, 0])

    return result
# 힙 쓸때는 계속 틀리더니 덱 쓰니까 바로 맞음.. 뭐지
