def sanitize(string):
    head, num, tail = '', '', ''
    tail_i = -1
    num_checked = False
    for idx, letter in enumerate(string):
        if letter.isdecimal():
            if not num_checked:
                num_checked = True
            num += letter
        else:
            if num_checked:
                tail_i = idx
                break
            else:
                head += letter
    if tail_i != -1:
        tail = string[tail_i:]
    return [head, num, tail]


def solution(files):
    answer, _files = [], []
    for file in files:
        _files.append(sanitize(file))
    _files = sorted(_files, key=lambda x: (x[0].upper(), int(x[1])))
    for _file in _files:
        answer.append(''.join(_file))
    return answer
