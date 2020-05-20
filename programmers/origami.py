def solution(n):
    result = [0]
    for i in range(1, n):
        sample = [0, 1] * ((len(result) + 1) // 2)
        idx = 0
        while sample:
            result.insert(idx, sample.pop(0))
            idx += 2
    return result

# 이건 두 테스트 케이스에서 시간초과가 떴다. 구현만으로는 해결되지 않는 문제.


def solution1(n):
    result = [0]
    for i in range(1, n):
        result = result + [0] + new(result)
    return result


def new(arr):
    arr.reverse()
    for i in range(len(arr)):
        if arr[i] == 1:
            arr[i] = 0
        else:
            arr[i] = 1
    return arr

# 종이 접기라서 가운데에 있는 0을 기준으로 대칭이 되는 형식이었기 때문에 0 의 오른쪽 부분은 왼쪽 부분을 역순으로 뒤집고 각 0, 1을 뒤집으면 대칭이 완성되는 식으로 구현해야했다.
