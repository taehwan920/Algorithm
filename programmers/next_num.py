# 다음 큰 숫자
# 문제 설명
# 자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

# 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
# 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
# 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
# 예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

# 자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.

# 제한 사항
# n은 1,000,000 이하의 자연수 입니다.


def solution(n):
    count = binary(n).count('1')  # 제시된 숫자의 이진수의 1의 개수 파악
    count_b = 0
    while count_b != count:  # 각 숫자를 이진수로 바꾸어 1의개수가 같은 숫자가 나올때까지 반복
        n += 1  # 주어진 수보다 1큰 수부터, 반복될때마다 자연수 하나씩 다 확인
        count_b = binary(n).count('1')  # 1의 개수를 계속 갱신.
    return n  # 조건에 해당하는 수 반환


def binary(num):  # 이진수 구하는 함수
    _num = num
    temp = []
    while _num > 1:
        if _num % 2 == 0:  # 나머지가 0이면 0을, 아니면 1을 임시 배열에 집어넣음.
            temp.append(0)
            _num = _num // 2
        else:
            temp.append(1)
            _num = _num // 2
    temp.reverse()  # 거꾸로 뒤집어야 제대로 이진수가 나온다.
    return list(map(str, temp))  # 배열로 반환
