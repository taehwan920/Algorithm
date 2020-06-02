e, f, c = map(int, input().split())


def new_bot(e, f):
    new = (e + f) // c
    empty = (e + f) % c
    if new + empty < c:
        return new
    else:
        return new + new_bot(new, empty)


print(new_bot(e, f))

# 처음에 생각없이 가진 병, 주운 병을 더해 필요한 병의 몫으로 했더니 틀렸었음.
# 빈병을 모아서 바꿔서 새로 받은 병을 다 마시고 생긴 빈병과 방금 전에 바꾸고 남은 빈병을 합쳐서 또 바꿀 수 있으므로 해당 조건식을 재귀로 구현.
