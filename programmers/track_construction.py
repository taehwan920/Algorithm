import heapq
from copy import deepcopy


def solution(board):
    n = len(board)
    board2 = deepcopy(board)
    q1, q2 = [], []
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    heapq.heappush(q1, [0, 0, 0, direction[0]])
    heapq.heappush(q2, [0, 0, 0, direction[1]])

    def bfs(arr, bo):
        while arr:
            now, y, x, dir_now = heapq.heappop(arr)
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if ny >= n or ny < 0 or nx >= n or nx < 0 or bo[ny][nx] == 1:
                    continue

                new_cost = now + 100 if (dy, dx) == dir_now else now + 600

                if bo[ny][nx] == 0:
                    heapq.heappush(arr, [new_cost, ny, nx, (dy, dx)])
                    bo[ny][nx] = new_cost
                elif new_cost < bo[ny][nx]:
                    heapq.heappush(arr, [new_cost, ny, nx, (dy, dx)])
                    bo[ny][nx] = new_cost

    bfs(q1, board)
    bfs(q2, board2)

    return min(board[n-1][n-1], board2[n-1][n-1])

# TC하나가 삑난 코드.
