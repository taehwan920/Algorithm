n = input()
num = [0 for i in range(9)]
for i in n:
    temp = int(i)
    if temp == 9:
        num[6] += 1
    else:
        num[temp] += 1
a, b = max(num[:6]), max(num[7:])
if num[6] % 2 == 0:
    if max(a, b) >= num[6] // 2:
        print(max(a, b))
    else:
        print(num[6] // 2)
else:
    if max(a, b) >= num[6] // 2 + 1:
        print(max(a, b))
    else:
        print(num[6] // 2 + 1)
