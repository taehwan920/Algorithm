n = int(input())
predict = []

for _ in range(n):
    predict.append(int(input()))

predict.sort()

result = 0
for i in range(1, len(predict)+1):
    result += abs(i - predict[i-1])

print(result)
