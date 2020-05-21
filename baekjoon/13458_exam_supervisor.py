n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

result = 0

for i in range(n):
    rest = a[i] - b
    if rest > 0:
        if rest % c == 0:
            result += rest // c
        else:
            result += (rest // c) + 1
    result += 1

print(result)

# 간단한 구현문제.
