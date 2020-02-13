# 문자열 다루기 기본
# 문제 설명
# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.

# 제한 사항
# s는 길이 1 이상, 길이 8 이하인 문자열입니다.


def solution(s):
    s = s.upper()
    answer = True
    if len(s) != 4 and len(s) != 6:
        answer = False
    else:
        for i in s:
            if ord("A") <= ord(i) <= ord("Z"):
                answer = False
                break
    return answer
# 숫자형만 들어있는지 확인하는 내장함수는 list.isdigit()임

# 이게 답


def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)
# len() in (4, 6)은 len()의 값이 4, 6 튜플 안에 포함되어 있는가 체크하는것;
