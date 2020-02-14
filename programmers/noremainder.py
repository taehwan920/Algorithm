# 나누어 떨어지는 숫자 배열
# 문제 설명
# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

# 제한사항
# arr은 자연수를 담은 배열입니다.
# 정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
# divisor는 자연수입니다.
# array는 길이 1 이상인 배열입니다.


def solution(arr, divisor):
    S = []
    for i in arr:
        if i >= divisor:
            if i % divisor == 0:
                S.append(i)
    S.sort()
    if len(S) == 0:
        S.append(-1)
    return S


# 다른사람의 풀이
def solution(arr, divisor): return sorted(
    [n for n in arr if n % divisor == 0]) or [-1]
# [n for n in arr if n%divisor == 0] n%divior==0인 arr의 요소를 리스트로 만드는 함수.
# sorted로 굳이 줄을 바꾸지 않고 정렬했다.
# or 는 앞의 함수가 거짓일 경우 뒤의 것을 호출하는 것..
