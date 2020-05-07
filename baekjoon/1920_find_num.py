N = int(input())

A = list(set(map(int, input().split())))

M = int(input())

nums = list(map(int, input().split()))

for i in nums:
    if i in A:
        print(1)
    else:
        print(0)

# 이런 찾는 문제는 찾아야하는 모집단을 가능한한 작게만드는 방법을 연구. 여기선 set을 사용.
