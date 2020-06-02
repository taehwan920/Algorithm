n, k = map(int, input().split())
if n == 1:
    print(1)
    exit(0)
medals = []
for i in range(n):
    medals.append(list(map(int, input().split())))

medals = sorted(medals, key=lambda x: x[3], reverse=True)
medals = sorted(medals, key=lambda x: x[2], reverse=True)
medals = sorted(medals, key=lambda x: x[1], reverse=True)
rank = 1
same = 0
if medals[0][0] == k:
    print(1)
else:
    for i in range(1, len(medals)):
        if medals[i][1:] == medals[i-1][1:]:
            same += 1
        else:
            rank += same + 1
            same = 0
        if medals[i][0] == k:
            print(rank)
            break
