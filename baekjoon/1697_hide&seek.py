n, k = map(int, input().split())
MAX = 100001
visited = [0] * MAX

q = [n]
while q:
    temp = q.pop(0)
    if temp == k:
        print(visited[temp])
        break
    for next_t in (temp-1, temp+1, temp*2):
        if 0 <= next_t < MAX and not visited[next_t]:
            visited[next_t] = visited[temp] + 1
            q.append(next_t)

# 숫자의 범위를 초과 하지 않도록 제한해 줄 필요가 있었음. ex) 0 <= next_t < MAX
