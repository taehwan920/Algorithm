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

# by selection sort
T = int(input())

nums = []
for i in range(T):
    new = int(input())
    nums.append(new)

for i in range(len(nums)):
    least = i
    for j in range(i + 1, len(nums)):
        if nums[least] > nums[j]:
            least = j
    nums[i], nums[least] = nums[least], nums[i]

for m in nums:
    print(m)
