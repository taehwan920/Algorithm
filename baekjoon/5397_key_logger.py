T = int(input())

for _ in range(T):
    logged = input()
    left = []
    right = []

    for i in logged:
        if i == "-":
            if left:
                left.pop()
        elif i == "<":
            if left:
                right.append(left.pop())
        elif i == ">":
            if right:
                left.append(right.pop())
        else:
            left.append(i)

    left.extend(reversed(right))

    print(''.join(left))

# 뭔가 입력하고 어쩌고 막 하는거는 스택 or 큐로 생각하자.. ㅜㅜ
