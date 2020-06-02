board = [[0 for i in range(100)] for i in range(100)]


def draw_rec(x, y):
    w_s, w_e = x, x + 10
    h_s, h_e = 100 - y, 100 - (y + 10)
    for i in range(h_s, h_e, -1):
        for j in range(w_s, w_e):
            board[i][j] = 1


result = 0
for i in range(int(input())):
    x, y = map(int, input().split())
    draw_rec(x, y)

for line in board:
    result += line.count(1)

print(result)
