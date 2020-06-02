for _ in range(int(input())):
    a, b = 0, 0
    for i in range(int(input())):
        x, y = map(float, input().split())
        a += x
        b += round(x * y, 1)
    a = int(a)
    print(a, round(b / a, 1))
