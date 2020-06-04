t, all_t = map(int, input().split())
task = list(map(int, input().split()))
cnt = 0
accum = 0
for i in range(len(task)):
    accum += task[i]
    if accum > all_t:
        cnt += i
        break
else:
    cnt += len(task)
print(cnt)
