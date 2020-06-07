for _ in range(int(input())):
    n, m = map(int, input().split())

    result = 1

    for i in range(n):
        result *= (m - i)
    for i in range(1, n+1):
        result //= i

    print(result)

# 그냥 순열 문제.
