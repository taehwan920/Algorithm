n, m = map(int, input().split())
see = {}
two = []
for i in range(n):
    see[input()] = 1
for i in range(m):
    hear = input()
    if hear in see:
        two.append(hear)
two.sort()
print(len(two))
for i in two:
    print(i)

# 해쉬 = 탐색의 왕
