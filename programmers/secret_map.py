# 문제 : https://programmers.co.kr/learn/courses/30/lessons/17681


def solution(n, arr1, arr2):
    num_li = []
    NUM_LI = []
    answer = []
    for i in range(n):  # 두 배열안에 있는 숫자를 전부 이진수로 변환
        num_li.append(binarize(arr1[i], n))
        NUM_LI.append(binarize(arr2[i], n))
    for j in range(n):  # 각 배열의 문자열들을 대조해 비밀지도 완성
        answer.append(examine(num_li[j], NUM_LI[j]))
    return answer


def binarize(num, N):  # 이진수로 만드는 함수를 정의
    arr = []  # 빈배열 준비
    _num_ = num  # 혹시모르니 새로 변수 정의해주기
    while True:
        if _num_ == 1:
            arr.append(_num_)
            break
        elif _num_ == 0:
            arr.append(_num_)  # 마지막 나머지를 이진수에 추가해주기위한 조건식
            break
        else:
            arr.append(_num_ % 2)  # 나눈 나머지들을 전부 배열에 때려박기
            _num_ = _num_ // 2  # 나눈 몫을 다시 활용하기 위해 변수 지정
    if len(arr) < N:  # 이진수를 지도로 활용해야 하기때문에 혹여 이진수가 너무 짧으면 그만큼 0을 추가해야함.
        for i in range(N - len(arr)):  # 모자란 자릿수 만큼 0을 추가하는 반복문
            arr.append(0)
    arr = list(map(str, arr))  # 활용이 쉽도록 배열을 문자열로 싹 바꿈
    arr.reverse()  # 이진수는 순서를 바꿔야 하므로 뒤집어주기

    return ''.join(arr)  # 연결된 문자열로 반환


def examine(s1, s2):  # 두 지도의 문자열을 대조하는 함수
    ex_arr = []
    for i in range(len(s1)):
        if s1[i] == '1' or s2[i] == '1':
            ex_arr.append("#")
        elif s1[i] == '0' and s2[i] == '0':
            ex_arr.append(' ')
    return ''.join(ex_arr)


# 다른사람의 풀이

def secret_map(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):  # zip을 사용해 arr1, arr2를 한꺼번에 활용
        # bin을 쓰면 그대로 이진수로 활용할수 있다.. 이상한 문자가 붙어있길래 안썼는데 슬라이싱으로 이상한 문자를 떼어버림. 그뒤 문자열로 변환
        a12 = str(bin(i | j)[2:])
        # rjust(n)은 해당 문자열을 n글자 개수로 만들기 위해 글자를 오른쪽으로 밀어버리고 왼쪽에 부족한  글자수만큼 공백을 추가해줌. 반대 함수인 ljust도 있음.
        a12 = a12.rjust(n, '0')
        # replace(찾을값, 바꿀값, (바꿀횟수))를 활용하여 1을 샵으로, 0을 공백으로 바꿔줌.
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    return answer
