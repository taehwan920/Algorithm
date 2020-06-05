from math import gcd


def solution(arr):
    arr.sort()
    while len(arr) > 1:
        temp = arr[0] * arr[1] // gcd(arr[0], arr[1])
        arr.pop(0)
        arr.pop(0)
        arr = [temp] + arr
    return arr[0]

# 최소공약수는 math모듈에 내장 메소드로 있음.
# 최대 공약수는 두 수를 곱해서 최대공약수로 나눠주면 구할 수 있음.
# 여러 수의 최소 공배수는 두개씩 짝지어 최소공배수를 구하면 됨.
