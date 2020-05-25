n, p = map(int, input().split())
_n = n
result = []
result.append(n)
while True:
    n = (n * _n) % p
    if n in result:
        idx = result.index(n)
        print(len(result[idx:]))
        break
    result.append(n)
