# 문제 : https://programmers.co.kr/learn/courses/30/lessons/17681


def solution(n, arr1, arr2):
    num_li = []
    NUM_LI = []
    answer = []
    for i in range(n):
        num_li.append(binarize(arr1[i], n))
        NUM_LI.append(binarize(arr2[i], n))
    print(num_li, NUM_LI)
    for j in range(n):
        answer.append(examine(num_li[j], NUM_LI[j]))
    return answer


def binarize(num, N):
    arr = []
    _num_ = num
    while True:
        if _num_ == 1:
            arr.append(_num_)
            break
        elif _num_ == 0:
            arr.append(_num_)
            break
        else:
            arr.append(_num_ % 2)
            _num_ = _num_ // 2
    if len(arr) < N:
        for i in range(N - len(arr)):
            arr.append(0)
    arr = list(map(str, arr))
    arr.reverse()

    return ''.join(arr)


def examine(s1, s2):
    ex_arr = []
    for i in range(len(s1)):
        if s1[i] == '1' or s2[i] == '1':
            ex_arr.append("#")
        elif s1[i] == '0' and s2[i] == '0':
            ex_arr.append(' ')
    return ''.join(ex_arr)
