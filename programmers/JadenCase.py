def solution(s):
    _s = list(map(list, s.split(' ')))
    for i in range(len(_s)):
        for j in range(len(_s[i])):
            if _s[i][j].isalpha():
                if j == 0:
                    _s[i][j] = _s[i][j].upper()
                elif _s[i][j].isupper():
                    _s[i][j] = _s[i][j].lower()
        _s[i] = ''.join(_s[i])
    return ' '.join(_s)

# s.split()으로 했을 땐 테스트케이스 중 몇개가 틀렸다고 나오는데, s.split(' ')으로 바꾸니 정답으로 떴다. 차이점을 연구해서 블로그에 써야겠다.
