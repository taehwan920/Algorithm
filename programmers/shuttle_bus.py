def solution(n, t, m, timetable):
    times = sorted(list(map(lambda x: transform(x), timetable)))
    get_on = 9 * 60
    result = 0
    while n > 0:
        if n == 1:
            if times[0] > get_on:
                result = get_on
                break
            else:
                if len(times) < m:
                    if len(times) == 0:
                        result = get_on
                        break
                    else:
                        MAX = max(times)
                        result = MAX if MAX >= 9 * 60 else 9 * 60
                        break
                else:
                    MAX = max(times[:m])
                    result = MAX - 1
                    break
        else:
            temp_m = m
            for i in range(temp_m):
                if len(times) == 0 or times[0] > get_on:
                    break
                times.pop(0)
        n -= 1
        get_on += t
    new_h = "0" + str(result // 60) if result // 60 < 10 else str(result // 60)
    new_m = "0" + str(result % 60) if result % 60 < 10 else str(result % 60)
    t_stamp = new_h + ":" + new_m
    return t_stamp


def transform(string):
    h, m = map(int, string.split(":"))
    return h * 60 + m
