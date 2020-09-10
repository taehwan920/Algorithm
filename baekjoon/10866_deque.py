from collections import deque
import sys
input = sys.stdin.readline

deq = deque([])

for _ in range(int(input())):
    temp = input().split()
    if len(temp) == 2:
        if temp[0] == 'push_front':
            deq.appendleft(int(temp[1]))
        else:
            deq.append(int(temp[1]))
    else:
        order = temp[0]
        if order == 'front':
            if deq:
                print(deq[0])
            else:
                print(-1)
            continue
        if order == 'back':
            if deq:
                print(deq[-1])
            else:
                print(-1)
            continue
        if order == 'size':
            print(len(deq))
            continue
        if order == 'pop_front':
            if deq:
                print(deq.popleft())
            else:
                print(-1)
            continue
        if order == 'pop_back':
            if deq:
                print(deq.pop())
            else:
                print(-1)
            continue
        if order == 'empty':
            print(0 if deq else 1)
