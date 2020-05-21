n = int(input())

men = list(map(int, input().split()))
line = [0 for i in range(n)]

for i in range(n):
    man = men[i]
    for j in range(n):
        if man > 0:
            if line[j] == 0:
                man -= 1
        else:
            if line[j] == 0:
                line[j] = i+1
                break

for i in line:
    print(i, end=' ')

# 구현문제인데 출력에서 헤매느라 계속 오답이 떴다.
