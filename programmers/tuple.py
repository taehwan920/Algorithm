def solution(s):
    to_li = list(map(str, s[2:-2].split('},{')))
    to_li = list(map(lambda x: x.split(','), to_li))
    to_li = sorted(to_li, key=lambda x: len(x))
    result = [int(to_li[0][0])]
    for i in range(1, len(to_li)):
        temp = list(filter(lambda x: x not in to_li[i-1], to_li[i]))
        result.append(int(temp[0]))
    return result

# 문자열 구현 문제는 split만 잘써도 해결된다.
