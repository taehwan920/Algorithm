# 소수 찾기
# 문제 설명
# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)

# 제한 조건
# n은 2이상 1000000이하의 자연수입니다.

import math


def prime(num):
    for i in range(3, int(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False
    return True


def solution(n):
    answer = 1
    for i in range(3, n+1, 2):
        if prime(i):
            answer += 1
    return answer

# 소수찾기 문제에선 짝수는 무조건 거르고 시작하면 효율성 두배
