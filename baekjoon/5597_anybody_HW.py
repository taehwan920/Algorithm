board = [0 for i in range(31)]
board[0] = 1

for i in range(28):
    board[int(input())] = 1

for i, num in enumerate(board):
    if num == 0:
        print(i)
