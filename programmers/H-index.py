def solution(cited):
    _c = sorted(cited, key=lambda x: x, reverse=True)

    for i, data in enumerate(_c):
        if data <= i:
            return i
    return len(cited)


# 문제 이해하는게 너무 난해해서 제대로 못풀었다.
