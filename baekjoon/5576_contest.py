w, k = [], []
for i in range(10):
    w.append(int(input()))
for j in range(10):
    k.append(int(input()))

w.sort()
k.sort()
print(sum(w[-3:]), sum(k[-3:]))
