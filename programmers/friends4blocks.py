# 문제 타입 = 구현
# 관건
# 1. 블록이 밑으로 떨어져야함
# 2. 2x2 블록이 겹쳐져 있을 경우 같이 터져야 함
# 1번 조건부터 보자면 주어진 board를 오른쪽으로 90도 회전시켜서 지워야 할 블록을 pop()시키는 것 만으로 굳이 블록이 내려가는 기능을 구현할 필요가 없어짐.
# 2번 조건은 2x2 블럭을 전부 체크해 한꺼번에 터트려야 함.
# 그래서 중복을 피하기 위해 set에 추가.
# board 순회가 끝나면 set안의 모든 요소들을 board에서 pop으로 제거. 이때 위쪽 블록부터 pop()해야 엉뚱한게 터지지 않으므로 정렬한번 해야함.
# 순회가 끝난 뒤 set가 텅 비어있다면 2x2블록이 없는것이므로 반복 종료.


class game:
    pending = set()
    cnt = 0
    board = []
# 클래스 하나 사용하는것 만으로 구현이 엄청나게 간단해졌다.


def bomb():
    for i, j in reversed(sorted(game.pending)):
        # pop시 가장 중요한건 순서임. 역순 정렬하면 같은 행이어도 더 뒤에있는 인덱스가 먼저 나오기때문에 다음과같이 정렬해줌.
        game.board[i].pop(j)
        game.cnt += 1
    game.pending = set()
    # set초기화.


def search(i, j):
    if j >= len(game.board[i+1]) - 1:
        return
    # bomb이 한번 실행되고나면 각 리스트의 길이가 제각각이기 때문에 혹시 j가 다음행의 길이보다 길 경우 에러가 뜨므로
    # j가 다음행 끝 인덱스보다 클 경우 무시하도록한다.
    if game.board[i][j] == game.board[i][j+1] == game.board[i+1][j] == game.board[i+1][j+1]:
        for x, y in [(i + 1, j + 1), (i + 1, j), (i, j + 1), (i, j)]:
            game.pending.add((x, y))


def solution(m, n, board):
    game.board = [[board[i][j] for i in reversed(range(m))] for j in range(n)]
    # 90도 회전하는 코드. range를 역순으로 도는건 range를 reverse하는걸로 간단 구현 가능.

    while True:
        for i in range(len(game.board) - 1):
            for j in range(len(game.board[i]) - 1):
                search(i, j)
        if not game.pending:
            break
        bomb()
    return game.cnt


# 이 밑으로는 다시 푼 것

class game1:
    nominee = set()
    cnt = 0
    board = []


def search1(i, j):
    if j >= len(game1.board[i+1]) - 1:
        return

    if game1.board[i][j] == game1.board[i+1][j] == game1.board[i][j+1] == game1.board[i+1][j+1]:
        for y, x in [(i, j), (i+1, j), (i, j+1), (i+1, j+1)]:
            game1.nominee.add((y, x))


def bomb1():
    for y, x in reversed(sorted(game1.nominee)):
        game1.board[y].pop(x)
        game1.cnt += 1
    game1.nominee = set()


def solution1(m, n, board):
    game1.board = [[board[i][j] for i in reversed(range(m))] for j in range(n)]

    while True:
        for i in range(len(game1.board)-1):
            for j in range(len(game1.board[i])-1):
                search1(i, j)
        if game1.nominee:
            bomb1()
        else:
            break
    return game1.cnt

#
