def solution(str1, str2):
    str1, str2 = list(str1), list(str2)
    _str1, _str2 = sanitize(str1), sanitize(str2)
    if _str1 == [] and _str2 == []:
        return 65536
    if len(_str1) < len(_str2):
        _str1, _str2 = _str1, _str2
    else:
        _str1, _str2 = _str2, _str1

    gyo = 0
    for i in range(len(_str1)):
        for j in range(len(_str2)):
            if _str2[j] != -1:
                if _str1[i] == _str2[j]:
                    gyo += 1
                    _str1[i], _str2[j] = 0, -1
    hap = len(_str1) + len(_str2) - gyo
    return int(gyo/hap*65536)


def sanitize(st):
    a = []
    for i in range(len(st)-1):
        temp = []
        for j in range(i, i+2):
            if ord('a') <= ord(st[j]) <= ord('z') or ord('A') <= ord(st[j]) <= ord('Z'):
                temp.append(st[j])
            else:
                temp = []
                break
        if temp:
            temp_str = ''.join(temp).upper()
            a.append(temp_str)
    return a
