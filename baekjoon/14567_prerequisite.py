import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lecture = [[] for i in range(n+1)]
counts = [0 for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    lecture[a].append(b)
    counts[b] += 1

q = []

for i in range(1, n+1):
    if counts[i] == 0:
        q.append([1, i])

result = [0 for i in range(n+1)]

while q:
    seme_now, node = q.pop(0)
    result[node] = seme_now
    for i in lecture[node]:
        counts[i] -= 1
        if counts[i] == 0:
            q.append([seme_now + 1, i])

for i in result[1:]:
    print(i, end=" ")
