n, m = map(int, input().split())
letters = [{} for i in range(m)]
strings = []
for i in range(n):
    temp = input()
    strings.append(temp)
    for j in range(m):
        if temp[j] in letters[j]:
            letters[j][temp[j]] += 1
        else:
            letters[j][temp[j]] = 1

for i in range(m):
    letters[i] = sorted(letters[i].items(), key=lambda x: (x[0], x[1]))
    # items() 메소드는 딕셔너리의 각 키/밸류를 튜플로 묶어 배열에 담아 반환해줌.
    # 정렬 람다함수에서 튜플로 묶어서 하면 앞에있는 게 우선순위. 여러번 정렬 안해도됨.

result = ""
cnt = 0
for i in range(m):
    result += max(letters[i], key=lambda x: x[1])[0]

for i in range(n):
    for j in range(m):
        if strings[i][j] != result[j]:
            cnt += 1
print(result)
print(cnt)
