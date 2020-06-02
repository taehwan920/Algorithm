score = []
for i in range(1, 9):
    score.append([int(input()), i])
score = sorted(score, key=lambda x: x[0])
result = 0
for i in score[3:]:
    result += i[0]
print(result)
new = sorted(score[3:], key=lambda x: x[1])
for i in new:
    print(i[1], end=" ")
