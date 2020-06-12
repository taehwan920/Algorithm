h, w = map(int, input().split())
tenki = [[-1 for i in range(w)] for j in range(h)]

for i in range(h):
    temp = list(input())
    cloud = -1
    for j in range(w):
        if temp[j] == '.':
            if cloud != -1:
                cloud += 1
                tenki[i][j] = cloud
        else:
            cloud = 0
            tenki[i][j] = cloud

for i in tenki:
    for j in i:
        print(j, end=" ")
    print()
