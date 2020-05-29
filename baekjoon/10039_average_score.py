result = 0
for i in range(5):
    temp = int(input())
    temp = temp if temp >= 40 else 40
    result += temp

print(result // 5)
