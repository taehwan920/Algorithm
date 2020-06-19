def solution(n, s):
    if n > s:
        return [-1]
    result = []
    while n > 0:
        if n == 1:
            result.append(s)
            n -= 1
        else:
            now = int(s / n)
            result.append(now)
            n -= 1
            s -= now
    return result

# 처음엔 재귀로 풀었는데 시간초과가 떠서 반복문으로 풀었음.
