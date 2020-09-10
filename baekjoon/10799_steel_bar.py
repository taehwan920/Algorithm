par = input()
stack = []

bar = 0
for i in range(len(par)):
    if par[i] == ")":
        stack.pop()
        if par[i - 1] == ")":
            bar += 1
            continue
        if stack and stack[-1] == "(":
            bar += len(stack)
    if par[i] == "(":
        stack.append("(")
print(bar)
