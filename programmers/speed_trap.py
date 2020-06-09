def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    result = 0
    last = - 30001
    for route in routes:
        if last < route[0]:
            result += 1
            last = route[1]
    return result

# 각 자동차의 진출 지점을 기준으로 정렬
# 각 자동차의 진입 지점이 마지막 방문한 곳보다 클 경우만 카메라를 새로 설치.
# 그리고 해당 자동차의 진출 지점을 마지막 카메라 위치로 설정. 왜냐면 해당 자동차의 진입 ~ 진출지점 사이에 진입 지점이 있는 모든 자동차는 같은 카메라에 찍힐 것이므로.
# 위 과정을 반복.
