T = int(input())

nums = []
for i in range(T):
    new = int(input())
    if nums:
        for j in range(len(nums)):
            if max(nums) < new:
                nums.append(new)
                break
            if nums[j] >= new:
                nums.insert(j, new)
                break
    else:
        nums.append(new)

for i in nums:
    print(i)
