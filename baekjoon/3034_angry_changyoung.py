n, w, h = map(int, input().split())
for _ in range(n):
    match = int(input())
    if match ** 2 <= w ** 2 + h ** 2:
        print('DA')
    else:
        print('NE')
