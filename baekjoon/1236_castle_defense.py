Y, X = map(int, input().split())

x_li = [0 for i in range(X)]
y_li = [0 for i in range(Y)]

for i in range(Y):
    lane = input()
    for j, p in enumerate(lane):
        if p == "X":
            x_li[j] = 1
            y_li[i] = 1

x_c = x_li.count(0)
y_c = y_li.count(0)
print(max(x_c, y_c))
