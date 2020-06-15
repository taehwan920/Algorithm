import math


def solution(n, stations, w):
    distance = []
    # 기지국의 전파 범위가 닿지않는 곳들의 거리들을 담을 배열
    for i in range(1, len(stations)):
        distance.append((stations[i] - w) - (stations[i - 1] + w) - 1)
        # 이전 기지국의 최대 전파 범위를 현재 기지국의 최소 전파 범위에서 빼준뒤 1을 또 빼준다. 1을 또 빼주는 이유는 전파가 닿지않는 범위를 정확히 구하기 위함.

    distance.append(stations[0] - w - 1)
    # 첫번재 아파트부터 첫 기지국까지의 범위
    distance.append(n - (stations[-1] + w))
    # 마지막 기지국부터 마지막 아파트까지의 범위

    result = 0
    for dist in distance:
        if dist <= 0:
            # 위 과정 중 구한 범위가 0이하일 경우 기지국을 설치할 필요가 없으므로 패스.
            continue
        result += math.ceil(dist / (1 + w * 2))
        # 범위가 아무리 작더라도 최소한 1은 있으므로 반올림이 아닌 '올림'을 해준다.
    return result

# 제한사항에 주어진 n의 크기가 엄청나게 크길래 이분탐색인가 하였지만 낚시였다. 그냥 수학적으로 접근해서 구현만 하면 풀리는 문제였음. 너무 알고리즘 풀이 방식에만 의존하지말자.
# 이 문제를 풀 때 또 하나 깨달은 것은 굳이 예외사항을 배열에 넣을때 적용하지 말고 배열엔 일단 다 넣은 뒤 예외사항은 따로 처리해두고 배열 요소들을 사용할 때 확인하는게 더 편하다는 점.
# 왜냐면 넣을 때 예외사항 다 처리하려면 배열이 너무 작을 경우 에러가 뜨거나 하는 것까지 전부 고려해야 하므로 넣을 때에는 일단 다 넣어두도록하자.
