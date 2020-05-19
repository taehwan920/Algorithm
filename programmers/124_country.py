def solution(n):
    result = ''
    while n > 0:
        n -= 1
        result = '124'[n % 3] + result
        n //= 3
    return ''.join(result)


# 각 자리수마다 1을 빼준 뒤 계산을 해야 제대로 나옴.
# 왜냐면 일반적인 삼진수와는 달리 0부터 시작하는게 아니라 1부터 시작하는게 124나라의 규칙이라서.
# 그렇게 구한 자리수를 계속 앞에다가 붙여줘야 하기때문에 result += 가 아닌 result = '124'[n % 3] + result 로 더해줌.
