# 문자열 내림차순으로 배치하기
# 문제 설명
# 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
# s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

# 제한 사항
# str은 길이 1 이상인 문자열입니다.


def solution(s):
    s = list(s)
    s.sort()
    s.reverse()
    return ''.join(s)

# join, sort, reverse,index, zip 등의 내장 함수 용법에 익숙해질 것

# 다른 사람 답


def solutions(s):
    return ''.join(sorted(s, reverse=True))

## sorted(list, reverse= True or False)
# 순서포함해서 한번에 설정 가능한 내장함수.
