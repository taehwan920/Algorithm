a, b = input().split()
result = []
for i in range(len(b)-len(a)+1):
    cnt = 0
    new_b = b[i:i+len(a)]
    for j in range(len(new_b)):
        if new_b[j] != a[j]:
            cnt += 1
    result.append(cnt)

print(min(result))

# 더 짧거나 같은 문자열인 a를 문자열 b의 첫글자부터 비교해보고, 두번째글자부터 비교해보는 식으로해서 가장 차이가 작은 수를 출력.
