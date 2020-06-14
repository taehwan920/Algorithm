from math import gcd
import math


def solution(w, h):
    _w, _h = w, h
    w, h = min(w, h), max(w, h)
    ya = math.gcd(w, h)
    w /= ya
    h /= ya
    gradient = round(h / w, 2)
    last = gradient
    cnt = math.ceil(last)
    while last < h:
        temp = math.floor(last)
        last += gradient
        if last > h:
            cnt += int(h - temp)
        else:
            cnt += int(math.ceil(last) - temp)
    return (_w * _h) - (cnt * ya)

# 위에건 내가 직접 푼 것. 테스트케이스중 절반만 정답이 떴다.
# 주어진 사각형을 최대공약수를 통해 같은 비율의 가장 작은 사각형으로 만들어 그 사각형에 직접 선을 그어 선이지나가는 사각형의 개수를 구해 빼는것이었는데
# 아무래도 소수를 이용하다보니 정확하지 않은 결과가 나와 오답처리됐던것 같다.


def solution1(w, h):
    yak = gcd(w, h)
    _w = w / yak
    _h = h / yak
    cut = _w + _h - 1
    return w * h - cut * yak

# 아주 중요한 규칙이 하나 있었는데 바로 가장 작은 사각형을 구해서 가로와 세로의 길이를 더한 후 1을 빼면 선이 지나는 사각형의 개수를 구할 수 있었다는 것.
# 그래서 같은 원리로 풀이했더니 정답.
