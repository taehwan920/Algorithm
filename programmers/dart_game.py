def solution(dartResult):
    lib = {
        'score': [],
        'bonus': [],
        'option': [1, 1, 1]
    }
    s_p = -1
    bonus = list("SDT")
    op = ['*', '#']
    score = ""
    for i in dartResult:
        if i.isdecimal():
            score += i
        else:
            if i in bonus:
                lib['bonus'].append(i)
                lib['score'].append(int(score))
                score = ""
                s_p += 1
            elif i in op:
                lib['option'][s_p] = i

    result = []
    for i in range(3):
        temp = lib['score'][i]
        if lib['bonus'][i] == "D":
            temp = temp ** 2
        if lib['bonus'][i] == "T":
            temp = temp ** 3
        if lib['option'][i] == "*":
            if len(result) != 0:
                result[-1] *= 2
                temp *= 2
            else:
                temp *= 2
        if lib['option'][i] == "#":
            temp *= -1
        result.append(temp)

    return sum(result)

# 반드시 한번만 실행돼야 하는건 한번만 실행되는애랑 같이 묶을 것.
