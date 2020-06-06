n, k = map(int, input().split())
number = input()

stack = []
for idx, num in enumerate(number):
    while stack and stack[-1] < num and k:
        stack.pop()
        k -= 1

    if k == 0:
        stack.append(number[idx:])
        break

    stack.append(num)

stack = stack[:-k] if k else stack
print(''.join(stack))

# 프로그래머스에서 똑같은 문제를 풀어봤는데도 바로 답이 튀어나오지 않았다.
# 하지만 접근법을 잊지 않고 다시 차근차근 풀었더니 답을 찾을 수 있었다.
# 풀었던 문제를 다시 한번 씩 풀어 보는게 생각보다 도움이 많이 되는 듯 하다.
