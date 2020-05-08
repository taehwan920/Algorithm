N = list(input())
N = list(map(int, N))


def q_sort(li):
    if len(li) <= 1:
        return li

    pivot = li[0]
    left = []
    right = []

    for i in range(1, len(li)):
        if li[i] < pivot:
            right.append(li[i])
        else:
            left.append(li[i])

    return q_sort(left) + [pivot] + q_sort(right)


end = q_sort(N)
_end = list(map(str, end))
answer = ''
for i in _end:
    answer += i

print(int(answer))
