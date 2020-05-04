def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

    return max(triangle[-1])

# 프로그래머스 정수 삼각형 문제. DP의 핵심은 작은것 -> 큰것으로 케이스를 확장시켜나가는 것. 이걸 잊지 말고 꼭 시도해보기
