def solution(number, k):
    stack = []
    for i, num in enumerate(number):
        while stack and stack[-1] < num and k:
            # 이 조건의 경우 앞에 있는 조건이 먼저 false가 뜰 경우 뒤에 있는 조건은 확인도 안하고 넘겨서 에러가 안뜸. 아주 중요한 스킬.
            # 스택에 요소가 있고 스택 가장 뒷 요소가 넣으려는 숫자보다 작고 k가 0이 아닐 경우에 스택pop을 하고 k를 1 줄인다.
            stack.pop()
            k -= 1

        if k == 0:
            stack.append(number[i:])
            break

        stack.append(num)

    stack = stack[:-k] if k > 0 else stack
    # k가 아직 남아있을 경우 남은 k 개수만큼 뒤에서부터 잘라줌. k가 남는 경우는 특정 숫자 이후로는 그 숫자보다 작은 것만 뒤에 붙어있다는 뜻이기 때문에 가차없이 잘라버려도 된다.
    result = ''.join(stack)
    return result

# 징그러운 그리디 알고리즘. 이번 유형은 사실 구현문제에 가까움.
