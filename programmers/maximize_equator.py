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
