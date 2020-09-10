from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

nums = deque([i for i in range(1, n+1)])

result = []
while nums:
    for _ in range(k-1):
        nums.append(nums.popleft())
    result.append(nums.popleft())

print('<' + str(result)[1:-1] + '>')
