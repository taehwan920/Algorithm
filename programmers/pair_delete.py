def solution(s):
    if len(s) == 1:
        return 0
    s = list(s)
    stack = []

    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        else:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
    if stack:
        return 0
    else:
        return 1

# 시간초과 안걸리게 짠 로직. 시간 복잡도 O(n)
# stack이 비어있으면 하나 넣고 없으면 맨 마지막것과 현재 문자 부분을 비교 후 같으면 stack 마지막 원소를 없애고 다르면 그 문자를 스택에 넣는다.
# 이렇게 하면 원본 리스트는 변하는 것 없이 글자 일치 여부를 검사할 수 있다.
# 검사가 끝난 뒤 문자가 남아있으면 모두 제거하는데 실패했으므로 0, 아니면 1을 반환.
