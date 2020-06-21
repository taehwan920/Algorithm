n = int(input())
nums = list(map(int, input().split()))
while len(nums) > 1:
    x = nums.pop(0)
    y = nums.pop(0)
    x, y = max(x, y), min(x, y)
    while True:
        remain = x % y
        if remain == 0:
            break
        else:
            x, y = y, remain
    nums.append(y)

for i in range(1, nums[0] + 1):
    if nums[0] % i == 0:
        print(i)

# math 모듈 gcd 메소드로 풀어도 되는데 일부러 이렇게 풀어봄
