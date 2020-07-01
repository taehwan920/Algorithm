n, a, b = map(int, input().split())

if n == 1:
    print(-1)
    exit(0)


def fight(num):
    return num // 2 if num % 2 == 0 else num // 2 + 1


cnt = 1
while fight(a) != fight(b):
    cnt += 1
    a, b = fight(a), fight(b)

print(cnt)

# (1, 2), (3, 4), (5, 6), (7, 8) ... 이 순서대로 1라운드 시합이 치러지고
#   (1   ,   2),    (3   ,   4) ... 이 순서대로 2라운드 시합이 치러지므로
# 부여받은 번호를 2로 나눠 떨어지는 수는 2로 나눈 몫을 그대로 번호로 부여받고, 나누어떨어지지않는 수는 2로 나눈 몫에 + 1
