def is_beau(string):
    stack = []
    for letter in string:
        if stack:
            if stack[-1] == letter:
                stack.pop()
                continue
        stack.append(letter)
    if stack:
        return False
    else:
        return True


n = int(input())
cnt = 0
for i in range(n):
    if is_beau(input()):
        cnt += 1

print(cnt)
