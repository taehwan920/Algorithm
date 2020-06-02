y, n = 0, 0
for i in range(int(input())):
    temp = int(input())
    if temp:
        y += 1
    else:
        n += 1
result = 'Junhee is cute!' if y > n else 'Junhee is not cute!'
print(result)
