import heapq
import sys
input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    heapq.heappush(a, int(input()))

for i in range(n):
    print(heapq.heappop(a))
