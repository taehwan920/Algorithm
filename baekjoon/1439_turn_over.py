s = input()
cnt0, cnt1 = 0, 0
start = s[0]
if start == '0':
    cnt0 += 1
else:
    cnt1 += 1

for i in range(1, len(s)):
    if s[i] != start:
        start = s[i]
        if start == '0':
            cnt0 += 1
        else:
            cnt1 += 1

print(min(cnt0, cnt1))

# 연속된 숫자를 뒤집는 횟수의 최소값을 구해야하기때문에 연속된 0 과 연속된 1의 개수를 구해 더 작은걸 출력해주면 되는 문제.
