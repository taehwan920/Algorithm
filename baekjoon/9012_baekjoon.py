# 문제
# 괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다.

# 여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다.

# 입력
# 입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다. 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 하나의 괄호 문자열의 길이는 2 이상 50 이하이다.

# 출력
# 출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다.


# 첫번째 답. 오답임. 이렇게 하면 ")""(" 이 순서로 들어온 경우를 거를 수 없음.
from sys import stdin

N = int(stdin.readline())


def is_VPS(s):
    check = 0
    for i in range(len(s)):
        if s[i] == "(":
            check += 1
        elif s[i] == ")":
            check -= 1
    if check != 0:
        return False
    else:
        return True


for i in range(N):
    PS = list(stdin.readline())
    if is_VPS(PS):
        print("YES")
    else:
        print("NO")


# 두번째 답. 경우의 수를 잘 생각했더니 정답을 찾을 수 있었다. 기타 오타에도 주의할 것.


N = int(stdin.readline())


def is_VPS(li):
    check = 0
    stack = []
    for i in range(len(li)):
        if li[0] == ")" or li[-1] == "(":
            return False
        if li[i] == "(":
            stack.append("(")
        if li[i] == ")":
            if len(stack) == 0:
                return False
            else:
                del stack[-1]
    if len(stack) == 0:
        return True
    else:
        return False


for i in range(N):
    PS = list(stdin.readline())
    if is_VPS(PS):
        print("YES")
    else:
        print("NO")
