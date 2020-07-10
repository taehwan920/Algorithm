from copy import deepcopy
from itertools import permutations


def chop_str(st):
    nums = []
    opers = []
    temp_num = ''
    for i in range(len(st)):
        if st[i].isdecimal():
            temp_num += st[i]
        else:
            opers.append(st[i])
            nums.append(int(temp_num))
            temp_num = ''
    nums.append(int(temp_num))
    return [nums, opers]


def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)


def solution(expression):
    nums, opers = chop_str(expression)
    uni_oper = set(opers)
    cases = list(permutations(list(uni_oper), len(uni_oper)))
    candidate = []

    for i in range(len(cases)):
        _n, _o = deepcopy(nums), deepcopy(opers)
        case = cases[i]
        for j in range(len(case)):
            for k in range(len(_o)):
                if _o[k] == case[j]:
                    if _o[k] == '+':
                        _n[k+1] = _n[k] + _n[k+1]
                        _n[k] = -1
                    elif _o[k] == '-':
                        _n[k+1] = _n[k] - _n[k+1]
                        _n[k] = -1
                    elif _o[k] == '*':
                        _n[k+1] = _n[k] * _n[k+1]
                        _n[k] = -1
                    _o[k] = ''
            _n = list(filter(lambda x: x != -1, _n))
            _o = list(filter(lambda x: x != '', _o))
        candidate.append(abs(_n[0]))

    return max(candidate)

# TC중 하나가 런타임 에러가 떴던 코드.


def chop_str(st):
    nums = []
    opers = []
    temp_num = ''
    for i in range(len(st)):
        if st[i].isdecimal():
            temp_num += st[i]
        else:
            opers.append(st[i])
            nums.append(int(temp_num))
            temp_num = ''
    nums.append(int(temp_num))
    return [nums, opers]


def solution(expression):
    nums, opers = chop_str(expression)
    uni_oper = set(opers)
    cases = list(permutations(list(uni_oper), len(uni_oper)))
    candidate = []

    for i in range(len(cases)):
        _n, _o = deepcopy(nums), deepcopy(opers)
        case = cases[i]
        for j in range(len(case)):
            for k in range(len(_o)):
                if _o[k] == case[j]:
                    if _o[k] == '+':
                        _n[k+1] = _n[k] + _n[k+1]
                        _n[k] = 1e9
                    elif _o[k] == '-':
                        _n[k+1] = _n[k] - _n[k+1]
                        _n[k] = 1e9
                    elif _o[k] == '*':
                        _n[k+1] = _n[k] * _n[k+1]
                        _n[k] = 1e9
                    _o[k] = ''
            _n = list(filter(lambda x: x != 1e9, _n))
            _o = list(filter(lambda x: x != '', _o))
        candidate.append(abs(_n[0]))

    return max(candidate)

# 정답 코드. 1e9부분이 -1이었는데 이렇게 하면 계산 도중 -1이 값으로 나와버리는 케이스가 있을 경우 멀쩡한 배열 요소 하나가 사라져버려서 런타임오류가 나왔던 것.
# True나 False로 수정했었으나 역시 1과 0으로 인식해버려서 그런지 런타임에러(아마 인덱스 에러일 것)가 나왔다. 그래서 그냥 무지 큰 수인 1e9를 넣음으로써 해결했다.
