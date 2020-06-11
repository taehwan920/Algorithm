n = int(input())
nums = []
for i in range(n):
    temp = list(map(int, input().split()))
    nums.append(temp)

for i in range(3):
    for j in range(n):
        temp = nums[j][i]
        if temp == 0:
            continue
        for k in range(n):
            if j == k:
                continue
            if temp == nums[k][i]:
                nums[j][i] = 0
                nums[k][i] = 0

for i in nums:
    print(sum(i))
