left, right = list(input()), []

for _ in range(int(input())):
    temp = input().split()
    if len(temp) == 2:
        left.append(temp[1])
    else:
        order = temp[0]
        if order == 'L':
            if left:
                right.append(left.pop())
        if order == 'D':
            if right:
                left.append(right.pop())
        if order == 'B':
            if left:
                left.pop()
right.reverse()
print(''.join(left) + ''.join(right))
