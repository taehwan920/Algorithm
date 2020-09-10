n = int(input())
grade = []

for i in range(n):
    name, score = input().split(' ', maxsplit=1)
    temp2 = list(map(int, score.split()))
    grade.append([name, temp2])

sort1 = sorted(grade, key=lambda x: x[0])
sort2 = sorted(sort1, key=lambda x: x[1][2], reverse=True)
sort3 = sorted(sort2, key=lambda x: x[1][1])
sort4 = sorted(sort3, key=lambda x: x[1][0], reverse=True)

for item in sort4:
    print(item[0])
