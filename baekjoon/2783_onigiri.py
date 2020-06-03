s25_x, s25_y = map(int, input().split())
least = s25_x * 1000 / s25_y
for i in range(int(input())):
    a, b = map(int, input().split())
    least = min(a * 1000 / b, least)

print(round(least, 2))
