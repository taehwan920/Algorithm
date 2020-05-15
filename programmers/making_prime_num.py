def solution(nums):
    memo = [False, False] + [True for i in range(2, 3001)]
    for idx, num in enumerate(memo):
        if num:
            k = idx * 2
            while k <= 3000:
                memo[k] = False
                k += idx

    def is_prime(num):
        if memo[num]:
            return True
        return False

    n = len(nums)
    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                temp = nums[i] + nums[j] + nums[k]
                if is_prime(temp):
                    count += 1
    return count
# 에라토스테네스의 체는 반드시 외워 둘 것
