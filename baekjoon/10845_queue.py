from collections import deque
import sys
input = sys.stdin.readline

q = deque([])

for _ in range(int(input())):
    temp = input().split()
    if len(temp) == 2:
        q.append(int(temp[1]))
    else:
        order = temp[0]
        if order == 'front':
            if q:
                print(q[0])
            else:
                print(-1)
            continue
        if order == 'back':
            if q:
                print(q[-1])
            else:
                print(-1)
            continue
        if order == 'size':
            print(len(q))
            continue
        if order == 'pop':
            if q:
                print(q.popleft())
            else:
                print(-1)
            continue
        if order == 'empty':
            print(0 if q else 1)
