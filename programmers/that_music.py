def solution(m, musicinfos):
    infos = sanitize(musicinfos)
    m = san_score(m)
    that = ''
    for info in infos:
        if m in info[1]:
            that = info[0]
            break
    if that:
        return that
    else:
        return "(None)"


def sanitize(arr):
    a = []
    for i in range(len(arr)):
        s, e, name, score = arr[i].split(',')
        s_h, s_m = map(int, s.split(":"))
        e_h, e_m = map(int, e.split(":"))
        time = (e_h - s_h) * 60 + e_m - s_m
        score = san_score(score)
        while len(score) < time:
            score += score
        if len(score) > time:
            score = score[:time]
        a.append([name, score, time])
    a = sorted(a, key=lambda x: x[2], reverse=True)
    return a


def san_score(st):
    st = list(st)
    sample = ["C", "D", "F", "G", "A"]
    change = ["H", "I", "J", "K", "L"]
    for i in range(len(st)):
        if st[i] == "#":
            for j in sample:
                if j == st[i-1]:
                    st[i-1] = change[sample.index(j)]
            st[i] = 0
    st = ''.join(list(filter(lambda x: x != 0, st)))
    return st
