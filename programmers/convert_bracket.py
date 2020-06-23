def solution(p):
    if p == "" or is_right(p):
        return p
    u, v = p[:bal(p)+1], p[bal(p)+1:]
    # 위치를 알아낸 균형잡힌 문자열을 제대로 쪼개려면 구한 인덱스에 +1을 해줘야함.
    if is_right(u):
        return u + solution(v)
    else:
        _u = list(u[1:-1])
        for i in range(len(_u)):
            _u[i] = ")" if _u[i] == "(" else "("
        return "" + "(" + solution(v) + ")" + ''.join(_u)


def is_right(string):
    _s = list(string)
    stack = []
    for i in _s:
        if i == ")":
            if len(stack) == 0:
                return False
            elif stack[-1] != "(":
                return False
            else:
                stack.pop()
        else:
            stack.append(i)
    return False if stack else True

# 더이상 분리할 수 없는 균형잡힌 괄호 문자열의 위치를 알아내서 분리할 수 있도록 한다.
# 만약 v에 더 분리할 수 있는 문자열이 나오면 재귀로 또 쪼갤테니 그리디하게 균형잡힌 문자열의 위치를 알아내도록 한다.


def bal(string):
    num = 0
    for idx, st in enumerate(string):
        if st == ")":
            num -= 1
        if st == "(":
            num += 1
        if num == 0:
            return idx

# 문제에서 상세히 알려주는대로 따라하기만 하면 되는 문제였다. 관건은 균형잡힌 문자열을 쪼개는 위치를 구하는것.


def solution1(p):
    if not p:
        return p
    bal = balanced(p)
    u, v = p[:bal+1], p[bal+1:]

    return u + solution(v) if is_right(u) else '(' + solution(v) + ')' + turn_over(u[1:-1])


def turn_over(st):
    result = ''
    for let in st:
        if let == "(":
            result += ')'
        else:
            result += '('
    return result


def balanced(st):
    cnt = 0
    for idx, bracket in enumerate(st):
        if bracket == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return idx


def is_right1(st):
    stack = []
    for let in st:
        if let == "(":
            stack.append(let)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
    return True

# 다시 한 번 풀었음. 구현만 하면되는 문제. 문제만 잘읽어도 되는데 전에 풀었던거 기억해서 풀어낸답시고 이상하게 풀어서 또 틀렸었다.
