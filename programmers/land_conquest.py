def solution(land):
    n = len(land)
    if n == 1:
        return max(land[0])

    for i in range(1, n):
        for j in range(4):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])

    return max(land[-1])

# 해당 인덱스만 빼고 고르는 방법을 잘 숙지해 둘 것. 절대로 값으로 핸들링하면 안 된다.
