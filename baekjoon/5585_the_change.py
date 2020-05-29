n = int(input())
n = 1000 - n
cnt = 0
for i in (500, 100, 50, 10, 5, 1):
    cnt += n // i
    n %= i
print(cnt)
