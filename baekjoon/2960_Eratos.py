n, k = map(int, input().split())

nums = [False] * 2 + [True for i in range(n-1)]
cnt = 0
for idx in range(2, n+1):
    for j in range(idx, n+1, idx):
        if nums[j]:
            nums[j] = False
            cnt += 1
            if cnt == k:
                print(j)
                exit(0)
