n = int(input())
crane = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
box = sorted(list(map(int, input().split())), reverse=True)

if max(box) > max(crane):
    print(-1)
    exit(0)

positions = [0] * n
checked = [False] * m

result = 0
count = 0

while True:
    if count == len(box):
        break
    for i in range(n):
        while positions[i] < len(box):
            if not checked[positions[i]] and crane[i] >= box[positions[i]]:
                checked[positions[i]] = True
                positions[i] += 1
                count += 1
                break
            positions[i] += 1
    result += 1

print(result)
