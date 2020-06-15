a, b, c = map(int, input().split())
b *= 2
c *= 3

trucks = []

for i in range(3):
    temp = list(map(int, input().split()))
    trucks.append(temp)

toll = 0
for i in range(2, 101):
    parked = 0
    for truck in trucks:
        if truck[0] < i and truck[1] >= i:
            parked += 1
    if parked == 1:
        toll += a
    elif parked == 2:
        toll += b
    elif parked == 3:
        toll += c

print(toll)

# 딱히 어려운 문제는 아니었으나 이상/이하, 미만/초과 조건을 잘 잡아줘야만 풀 수 있는 문제였다.
