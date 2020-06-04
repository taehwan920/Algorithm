n = int(input())
seat = list(input())
cnt = 0
ls = 0

for i in range(len(seat)):
    if seat[i] == 'L':
        ls += 1
    else:
        cnt += 1

cnt += ls // 2 + 1 if ls // 2 != 0 else 0
# 첫 커플석 이외의 커플석은 전부 한명밖에 컵홀더를 못씀. 그래서 위와 같이 카운팅을 해주고, 만약 커플석이 전혀 없는 경우라면 굳이 이렇게 더할 이유가 없으므로 0을 더해주는식으로.
print(cnt)
