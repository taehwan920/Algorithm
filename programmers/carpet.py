def solution(brown, red):
    browns = yaksu(brown)
    reds = yaksu(red)
    is_there = []
    for i in range(len(browns)):
        for j in range(len(reds)):
            b_width = browns[i][0]
            r_width = reds[j][0]
            b_height = browns[i][1]
            r_height = reds[j][1]
            b_size = 2 * (b_width + b_height)
            r_size = 2 * (r_width + r_height + 4)
            if b_size == r_size:
                is_there.append([r_width+2, r_height+2])

    return is_there[0]


def yaksu(num):
    if num == 1:
        return [[1, 1]]
    temp = []
    for i in range(1, num):
        if num % i == 0:
            if [i, num / i] not in temp:
                temp.append([i, int(num / i)])
                temp.append([int(num / i), i])
            else:
                break
    temp.sort()
    len_half = int(len(temp) / 2)
    if len(temp) % 2 == 0:
        temp = temp[len_half:]
    else:
        temp = temp[len_half - 1:]
    return temp

# 모든 경우의수를 생각하는 버릇
# 완전탐색만 잘해도 본전은 건진다
