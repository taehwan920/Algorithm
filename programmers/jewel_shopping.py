def solution(gems):
    n = len(gems)
    all_n = len(set(gems))
    shortest = [n, 1e9, 1e9]
    l, r = 0, 0
    while 0 <= l < n and 0 <= r < n:
        bag = gems[l:r+1]
        if len(set(bag)) == all_n:
            if len(bag) < shortest[0]:
                shortest = [len(bag), l, r]
            elif len(bag) == shortest[0] and l <= shortest[1]:
                shortest = [len(bag), l, r]
            l += 1
        elif len(set(bag)) < all_n:
            r += 1
    return [shortest[1]+1, shortest[2]+1]

# 정확성은 다 맞았는데 효율성에서 틀림. 좀 더 고민해야함
