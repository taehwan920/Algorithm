# 팩토리얼


N = int(input())


def factorial(i):
    if i <= 1:
        return 1
    if i > 1:
        return i * factorial(i-1)


print(factorial(N))
