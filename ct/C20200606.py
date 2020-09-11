# 1번

import heapq
import sys
pw = input()
judge = [False] * 5

if len(pw) >= 10:
    judge[4] = True

for letter in pw:
    if letter.isdecimal():
        judge[2] = True
    if ord('a') <= ord(letter) <= ord('z'):
        judge[0] = True
    if ord('A') <= ord(letter) <= ord('Z'):
        judge[1] = True
    if not letter.isdecimal() and not letter.isalpha():
        judge[3] = True

lev = judge.count(True)
print(f"LEVEL{lev}")

# adfkdncjdk

# LEVEL2

# Aei0#

# LEVEL4

# aq%~9P2!@@s!v#&&KM^lFf

# LEVEL5

# 2번

n = int(input())
game = {}

for i in range(n*(n-1)):
    t1, s1, t2, s2 = input().split()
    s1, s2 = int(s1), int(s2)
    t1_w = 1 if s1 > s2 else 0
    t2_w = 1 if s2 > s1 else 0
    if t1 not in game:
        game[t1] = [t1_w, s1 - s2]
    else:
        game[t1][0] += t1_w
        game[t1][1] += s1 - s2
    if t2 not in game:
        game[t2] = [t2_w, s2 - s1]
    else:
        game[t2][0] += t2_w
        game[t2][1] += s2 - s1

game = sorted(game.items(), key=lambda x: x[0])
game = sorted(game, key=lambda x: (x[1][0], x[1][1]), reverse=True)
for i in game:
    print(i[0], i[1][0], i[1][1])

# 3
# a 2 b 0
# a 2 c 1
# b 2 a 1
# b 0 c 2
# c 0 a 2
# c 1 b 2

# a 3 4
# b 2 -2
# c 1 -2

# 4
# drx 2 t1 1
# drx 1 gen 2
# t1 1 gen 2
# t1 2 drx 1
# kt 1 drx 2
# t1 0 kt 2
# drx 2 kt 1
# gen 1 t1 2
# gen 2 kt 0
# gen 1 drx 2
# kt 0 t1 2
# kt 2 gen 0

# drx 4 2
# gen 3 0
# t1 3 0
# kt 2 -2

# 3번

n, k = map(int, input().split())
pepero = []
for i in range(n):
    pepero.append(round(float(input()), 2))

start = 0
end = max(pepero)
while start <= end:
    mid = round((start + end) / 2, 2)
    cnt = 0
    for pepe in pepero:
        if pepe >= mid:
            cnt += int(pepe // mid)

    if cnt >= k:
        start = mid + 0.01
    else:
        end = mid - 0.01

print(round(start, 2))

# 2 3
# 6.3
# 4.3

# 3.15

# 18 300
# 51.28
# 96.87
# 96.86
# 48.63
# 87.83
# 51.29
# 56.72
# 38.05
# 3.88
# 79.40
# 33.43
# 30.75
# 13.12
# 67.80
# 20.15
# 96.71
# 95.93
# 10.91

# 3.20

# 4번
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n, m = map(int, input().split())
train = {}
distance = {}
for i in range(m):
    s, e, w = input().split()
    w = int(w)
    if s not in train:
        train[s] = [[w, e]]
        distance[s] = 1e9
    else:
        train[s].append([w, e])
    if e not in train:
        distance[e] = 1e9


def djik(start, end):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0
    for i in distance:
        if distance[i] != 1e9:
            distance[i] = 1e9
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in train[now]:
            cost = i[0] + dist
            if distance[i[1]] > cost:
                distance[i[1]] = cost
                if i[1] == end:
                    return cost
                if i[1] not in train:
                    continue
                heapq.heappush(q, (cost, i[1]))
    return -1


for i in range(int(input())):
    start, end = map(str, input().split())
    if start == end:
        print(0)
    elif start in train:
        print(djik(start, end))
    else:
        print(-1)

# 2 4
# ox oo 4
# ox xo 4
# xx ox 1
# xo oo 3
# 3
# xo oo
# oo xx
# xx oo

# 3
# -1
# 5

# 3 9
# xoo oox 4
# ooo xox 4
# oxx xoo 5
# oox ooo 3
# ooo xxo 3
# xox xoo 3
# oxo xoo 4
# ooo oox 4
# ooo oxx 5
# 3
# oxo oox
# ooo oox
# xxx xox

# 8
# 4
# -1

# 3 6
# xxx xxo 4
# oxo ooo 5
# xoo oox 5
# xxo xox 2
# xoo oxo 4
# oxo xxo 1
# 4
# xox xoo
# oox xxo
# oxx oxx
# xoo ooo

# -1
# -1
# 0
# 9
