cups = [1, 0, 0]
for _ in range(int(input())):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    cups[a], cups[b] = cups[b], cups[a]

print(cups.index(1) + 1)
