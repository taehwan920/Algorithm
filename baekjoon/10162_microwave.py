import sys
input = sys.stdin.readline

t = int(input())

btns = [300, 60, 10]
if t % btns[2] != 0:
    print(-1)

else:
    result = []
    for btn in btns:
        result.append(t // btn)
        t = t % btn

    for i in result:
        print(i, end=" ")
