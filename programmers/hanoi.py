def solution(n):
    result = []

    def hanoi(n, a, b, c):
        if n == 1:
            result.append([a, c])
        else:
            hanoi(n-1, a, c, b)
            result.append([a, c])
            hanoi(n-1, b, a, c)

    hanoi(n, 1, 2, 3)
    return result
