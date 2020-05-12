t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    a %= 10
    if a == 0:
        print(10)
    if a == 1 or a == 5 or a == 6:
        print(a)
    if a == 2 or a == 3 or a == 7 or a == 8:
        print((a ** (b % 4 if b % 4 != 0 else 4)) % 10)
    if a == 4 or a == 9:
        print((a ** (b % 2 if b % 2 != 0 else 2)) % 10)
