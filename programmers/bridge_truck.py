def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    time = 0
    total_w = 0
    while truck_weights:
        time += 1
        get_out = bridge.pop(0)
        total_w -= get_out
        if total_w + truck_weights[0] <= weight:
            get_on = truck_weights.pop(0)
            bridge.append(get_on)
            total_w += get_on
        else:
            bridge.append(0)
    time += bridge_length
    return time

# 다리의 현재 무게를 계속 sum()을 사용해서 구한 것 때문에 시간초과가 떴었다.
# 이런 경우엔 따로 변수를 저장해서 다리의 무게를 캐싱하는것이 좋음.
