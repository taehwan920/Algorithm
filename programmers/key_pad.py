def solution(numbers, hand):
    result = ''
    pad = []
    for i in range(3):
        for j in range(3):
            pad.append([i, j])
    pad = [[3, 1]] + pad

    last_l, last_r = [3, 0], [3, 2]
    for i in range(len(numbers)):
        num = numbers[i]
        if num in [1, 4, 7]:
            result += 'L'
            last_l = pad[num]
        elif num in [3, 6, 9]:
            result += 'R'
            last_r = pad[num]
        else:
            l_dist, r_dist = get_dist(
                pad[num], last_l), get_dist(pad[num], last_r)
            if l_dist == r_dist:
                if hand == 'left':
                    result += 'L'
                    last_l = pad[num]
                else:
                    result += 'R'
                    last_r = pad[num]
            elif l_dist < r_dist:
                result += 'L'
                last_l = pad[num]
            else:
                result += 'R'
                last_r = pad[num]

    return result


def get_dist(coor1, coor2):
    return abs(coor1[0] - coor2[0]) + abs(coor1[1] - coor2[1])

# 시험봤던 문제. 그때도 쉬웠으니 지금도 쉽게 풀었다.
