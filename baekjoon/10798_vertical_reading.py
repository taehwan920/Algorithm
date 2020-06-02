string = ['' for i in range(75)]

for i in range(5):
    temp = list(input())
    for j in range(15):
        string[i+(j*5)] = temp.pop(0)
        if len(temp) == 0:
            break
print(''.join(string))
