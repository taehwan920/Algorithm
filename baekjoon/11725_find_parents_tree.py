n = int(input())

tree = [[] for i in range(n+1)]
result = [0 for i in range(n+1)]
result[1] = 1

for i in range(n-1):
    a, b = map(int, input().split(' '))
    tree[a].append(b)
    tree[b].append(a)


q = [1]
while q:
    now = q.pop(0)
    for node in tree[now]:
        if result[node]:
            continue
        result[node] = now
        q.append(node)

for parent in result[2:]:
    print(parent)
