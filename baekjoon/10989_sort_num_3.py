import sys
input = sys.stdin.readline

n = int(input())

arr = [0 for i in range(10 ** 4 + 1)]

for i in range(n):
    arr[int(input())] += 1

for i in range(len(arr)):
    if arr[i]:
        for j in range(arr[i]):
            print(i)


# 계수 정렬의 힘!
