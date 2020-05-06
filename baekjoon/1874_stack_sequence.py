N = int(input())

stack = []
result = []
num = 1

for i in range(1, N+1):
    new = int(input())

    while num <= new:
        stack.append(num)
        num += 1
        result.append('+')
    if stack[-1] == new:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        exit(0)

print('\n'.join(result))
