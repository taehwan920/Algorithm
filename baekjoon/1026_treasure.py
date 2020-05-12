n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

new_a = [0] * n
_a = list(a)
_b = list(b)
result = 0

for i in range(n):
    b_idx = _b.index(max(_b))
    a_idx = _a.index(min(_a))
    new_a[b_idx] = min(_a)
    _b[b_idx] = -1
    _a[a_idx] = 100

for i in range(n):
    result += new_a[i] * b[i]

print(result)
# 문제에 함정이 있었음. 그냥 하나는 정렬, 하나는 역순정렬해서 서로 곱해주면 더 간단하게 풀 수 있었다.
