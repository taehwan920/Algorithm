import sys
n = int(sys.stdin.readline())
a, b = 1, 2
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    for i in range(2, n):
        new = (a + b) % 10
        a, b = b, new
    print(b)

# 피보나치 수열 문제지만 마지막 자리수(1의 자리수)만 출력하는 되는 문제라 배열도 필요없이 변수 저장식 + 10으로 나눈 나머지만 활용해야 시간 초과 없이 풀 수 있는 문제 였다.
