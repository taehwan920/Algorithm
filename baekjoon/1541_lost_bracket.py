n = input()

n = list(map(str, n.split('-')))
n = list(map(lambda x: list(map(int, x.split('+'))), n))

result = sum(n[0])
for i in range(1, len(n)):
    result -= sum(n[i])

print(result)

# 구현으로 쉽게 풀 수 있는 그리디 알고리즘 문제.
