def solution(arr):
    if len(arr) == 0:
        return 0
    stack = []
    sticks = 0
    for i in range(len(arr)):
        if arr[i] == ")":
            if arr[i-1] == "(":
                stack.pop()
                sticks += len(stack)
            else:
                stack.pop()
                sticks += 1
        else:
            stack.append(arr[i])
    return sticks
