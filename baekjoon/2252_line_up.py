import sys
input = sys.stdin.readline


n, m = map(int, input().split())

student = [[] for i in range(n+1)]
indegree = [0 for i in range(n+1)]
q = []
result = []

for i in range(m):
    i, j = map(int, input().split())
    student[i].append(j)
    indegree[j] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    for i in q:
        temp = q.pop(0)
        result.append(temp)
        for j in student[temp]:
            indegree[j] -= 1
            if indegree[j] == 0:
                q.append(j)

for i in result:
    print(i, end=' ')
