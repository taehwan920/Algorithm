def solution(n, words):
    gamer = [0] * n
    gamer[0] = 1
    spoken = [words[0]]
    result = []

    for i in range(1, len(words)):
        gamer[i % n] += 1
        if words[i] in spoken:
            result = [(i % n)+1, gamer[i % n]]
            break
        else:
            spoken.append(words[i])
        if words[i-1][-1] != words[i][0]:
            result = [(i % n)+1, gamer[i % n]]
            break
    else:
        result = [0, 0]

    return result
