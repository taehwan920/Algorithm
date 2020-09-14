# 1


from itertools import combinations


def remove_dot(li):
    if li and li[0] == '.':
        li = li[1:]
    if li and li[-1] == '.':
        li = li[:-1]
    return li


def solution(new_id):
    new_id = list(new_id)
    special = ['-', '_', '.']

    fil1 = []
    for let in new_id:
        temp = let
        if temp.isalpha():
            if temp.isupper():
                temp = temp.lower()
            fil1.append(temp)
            continue
        if temp in special or temp.isdecimal():
            fil1.append(temp)

    fil2 = []
    for i in range(len(fil1)):
        if fil1[i] == '.':
            if fil2 and fil2[-1] == '.':
                continue
        fil2.append(fil1[i])

    fil2 = remove_dot(fil2)

    if len(fil2) == 0:
        fil2 = ['a', 'a', 'a']

    if len(fil2) >= 16:
        fil2 = remove_dot(fil2[:15])

    if len(fil2) <= 2:
        for i in range(3 - len(fil2)):
            fil2.append(fil2[-1])

    return ''.join(fil2)

# 2


def solution(orders, course):
    result = []

    for num in course:
        dic = {}
        for order in orders:
            temp = list(order)
            combi = list(combinations(temp, num))
            for item in combi:
                joined = ''.join(sorted(item))
                if dic.get(joined):
                    dic[joined] += 1
                else:
                    dic[joined] = 1
        dic_li = list(dic.items())
        if dic_li:
            most = max(dic_li, key=lambda x: x[1])
            for item in dic_li:
                if item[1] < 2:
                    continue
                if item[1] == most[1]:
                    result.append(item[0])

    return sorted(result)
