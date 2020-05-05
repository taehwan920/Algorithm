def solution(N, S):
    rates = [0 for i in range(N)]
    result = []
    S = list(map(lambda x: x - 1, S))
    S.sort()

    for i in range(N + 1):
        if i != N:
            fail = S.count(i)
            been = len(list(filter(lambda x: x >= i, S)))
            if fail != 0 and been != 0:
                rates[i] = fail / been

    for i in range(N):
        temp = rates.index(max(rates))
        result.append(temp + 1)
        rates[temp] = -1

    return result

# 로직은 맞았지만 테스트케이스 9번에서 시간초과가 떠서 실패.


def solution2(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x: result[x], reverse=True)

# 이건 다른 사람의 풀이. dict 자료형 활용할 생각을 꿈에도 못했다. 문제를 이번에도 꼼꼼히 읽지 못해서 많이 생각이 꼬여버린듯.
# 좀더 신중하게 생각하고 신중하게 읽어보자.
