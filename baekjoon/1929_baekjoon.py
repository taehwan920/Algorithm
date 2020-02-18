# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000)

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

from sys import stdin
import math

M, N = map(int, stdin.readline().split())


def is_prime(num):
    if num != 1:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
    else:
        return False
    return True


for i in range(M, N+1):
    if is_prime(i):
        print(i)

# 시간 복잡도를 줄이는 방법을 최대한 동원해서 풀것.
# 1. stdin.readline()을 이용
# 2. 테스트케이스 숫자가 너무 클 땐 가능하다면 제곱근을 이용해서 풀것.
