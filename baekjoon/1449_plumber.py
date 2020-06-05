n, l = map(int, input().split())
leak = list(map(int, input().split()))
leak.sort()

cnt = 0

temp = 0
for pipe in leak:
    if temp < pipe:
        cnt += 1
        temp = pipe + l - 1

print(cnt)

# 그리디 알고리즘 = 매 순간의 최적해가 전체의 최적해가 되는 마법
# 구멍난 곳을 정렬해준다
# temp변수는 테이프의 길이에서 여유분 길이를 뺀 값을 더해줌. 왜냐면 구멍난 위치를 시작점으로 삼고 여유분을 뺀 길이만큼 테이프를 붙이기 위함.
# 붙인 테이프의 끝 좌표보다 작은 좌표값은 무시해도 됨.
