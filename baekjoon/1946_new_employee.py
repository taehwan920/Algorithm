t = int(input())

for _ in range(t):
    n = int(input())
    rec = []
    for i in range(n):
        rec.append(list(map(int, input().split())))
    rec = sorted(rec, key=lambda x: x[0])
    last = rec[0][1]
    cnt = 1
    for i in rec:
        if i[1] < last:
            last = i[1]
            cnt += 1
    print(cnt)
