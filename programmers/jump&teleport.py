def solution(n):
    count = 0
    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            count += 1
    return count

# 동적계획법 문제지만 굳이 일일이 값을 memoization하지 않아도 풀 수 있는 문제 였다.
# 어떻게 보면 그냥 구현문제이기도 했음.
