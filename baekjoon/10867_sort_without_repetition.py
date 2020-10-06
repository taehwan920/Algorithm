n = int(input())

nums = list(set(map(int, input().split())))
nums.sort()

for num in nums:
    print(num, end=" ")
