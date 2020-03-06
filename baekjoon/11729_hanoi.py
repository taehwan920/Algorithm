def hanoi(n, a, b, c):
    if n == 1:
        move.append([a, c])
    else:
        hanoi(n-1, a, c, b)
        move.append([a, c])
        hanoi(n-1, b, a, c)


move = []
hanoi(int(input()), 1, 2, 3)

print(len(move))
for row in move:
    print(" ".join(str(i) for i in row))

# 누군가한테 설명할수 있을 정도로 숙지해둘것
