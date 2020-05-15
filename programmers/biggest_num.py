def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x: x*3, reverse=True)
    while numbers:
        if numbers[0] == '0':
            numbers.pop(0)
        else:
            break
    if numbers:
        numbers = ''.join(numbers)
    else:
        numbers = '0'
    return numbers

# 문자열은 곱셈을 하면 '3' * 3 == '333' 이 되고 '30' * 3 == '303030'이 된다.
# 그리고 정렬이 맨 앞자리 부터 들어가므로 '333'이 '303030'보다 크다. 이 두 성질을 이용해야 풀 수 있는 문제.
