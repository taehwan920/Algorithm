def solution(numbers):
    result = {}
    l = len(numbers)
    for i in range(l-1):
        for j in range(i+1, l):
            temp = numbers[i] + numbers[j]
            result[temp] = 1

    return sorted(list(result.keys()))
