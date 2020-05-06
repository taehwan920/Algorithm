while True:
    stack = []
    st = input()
    check = True
    if st == ".":
        break

    for i in st:
        if i == "(" or i == "[":
            stack.append(i)

        elif i == ")":
            if stack:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    check = False
            else:
                check = False

        elif i == "]":
            if stack:
                if stack[-1] == "[":
                    stack.pop()
                else:
                    check = False
            else:
                check = False

    if check and not stack:
        print("yes")
    else:
        print("no")

# 스택, 큐 문제는 문제만 잘읽어도 반은 감. 좀 더 사고방식이 컴퓨터 스러워졌으면 좋겠다.
