# 로봇 청소기가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.

# 로봇 청소기가 있는 장소는 N×M 크기의 직사각형으로 나타낼 수 있으며, 1×1크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 벽 또는 빈 칸이다. 청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북중 하나이다. 지도의 각 칸은 (r, c)로 나타낼 수 있고, r은 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로 부터 떨어진 칸의 개수이다.

# 로봇 청소기는 다음과 같이 작동한다.

# 1. 현재 위치를 청소한다.
# 2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
#   2-a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
#   2-b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
#   2-c. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
#   2-d. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
# 로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며, 벽을 통과할 수 없다.

# 입력
# 첫째 줄에 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 50)

# 둘째 줄에 로봇 청소기가 있는 칸의 좌표 (r, c)와 바라보는 방향 d가 주어진다. d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것이다.

# 셋째 줄부터 N개의 줄에 장소의 상태가 북쪽부터 남쪽 순서대로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다. 빈 칸은 0, 벽은 1로 주어진다. 지도의 첫 행, 마지막 행, 첫 열, 마지막 열에 있는 모든 칸은 벽이다.

# 로봇 청소기가 있는 칸의 상태는 항상 빈 칸이다.


import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())
y, x, d = map(int, input().split())
board = [list(map(int, input().split())) for i in range(n)]
turn = [(0, -1), (-1, 0), (0, 1), (1, 0)]
rear = [(1, 0), (0, -1), (-1, 0), (0, 1)]
# 청소하지 않은 곳은 0, 벽은 1이므로 벽이 아니면서 청소가 완료된곳은 2로 표시하기로 했다. 그래서 visited 배열을 따로 작성하지않음.
# 각 방향별 반대 방향을 지정해야 하기 때문에 왼쪽 방향으로 돌아야하는 rear 배열을 따로 만들었다.


def set_di(di):
    new_turn = (turn * 2)[di:di+4]
    return new_turn
# 각 방향별로 인덱스0이 왼쪽이 되도록 설정하기 위한 함수.
# 하지만 음수 나눗셈의 나머지를 활용하여 방향을 설정할 수 있었기 때문에 이 함수는 쓸모없어졌다.


def dfs(y, x, head):
    if board[y][x] == 0:
        board[y][x] = 2
        # 청소가 완료됐으며 벽이 아닌곳은 2로 표시한다.
    dy, dx = turn[head]
    ny, nx = y + dy, x + dx
    by, bx = rear[head]
    cant_move = True
    # 가장 어렵게 느껴졌던 부분. 네 방향 모두 청소가 돼있거나 벽이면서 후진도 할 수 없는 경우를 어떻게 구현해야할까 굉장히 고심했다.
    for ty, tx in turn:
        if board[y+ty][x+tx] == 0:
            cant_move = False
            break
    # 일단 한바퀴씩 돌려보면서 청소 안한 구역이면서 벽이 아닌 부분이 나오면 이동가능하다는 소리이므로 cant_move 변수를 False로 바꾸었다.

    if 0 <= ny < n and 0 <= nx < m:
        if board[ny][nx] == 0:
            # 2-a 조건. ny, nx는 현재 보고있는 방향에서 왼쪽방향에 있는 타일임.
            new_head = (head - 1) % 4
            # 음수의 나머지를 사용하여 보고있던 방향이 0일 경우에 왼쪽을 보면 방향이 3이 되도록 했음.
            # 음수의 나머지는 나누는 수보다 작을 경우 해당 음수에 나누는 수를 더하여 나온 수가 나머지 값으로서 도출된다.
            # 그래서 head가 0이었을 경우 1을 빼고 그걸 4로 나눈 나머지를 new_head로 하면 new_head는 3이 나온다.
            dfs(ny, nx, new_head)
        else:
            # 해당 타일이 벽이거나 청소가 끝난 경우
            if cant_move:
                # 4방향이 전부 벽이거나 청소가 끝난 경우
                if board[y+by][x+bx] != 1:
                    # 후진할 타일이 벽이 아닌 경우, 즉 2-c
                    dfs((y + by), (x + bx), head)
                # 2-d는 굳이 표기하지 않았다.
            else:
                # 2-b 조건. 해당 타일이 벽도, 청소 완료된 타일도 아니지만 그렇다고 이동할 수 없는 타일인 것도 아님. 즉 이동 가능.
                new_head = (head - 1) % 4
                dfs(y, x, new_head)


dfs(y, x, d)
result = 0
for i in board:
    result += i.count(2)
# 청소 완료된 공간의 개수를 물어보는 문제이므로 2의 개수를 합산해서 출력.
print(result)
