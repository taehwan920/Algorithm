n = int(input())
cnt = 0

for i in range(1, n+1):
    for j in range(i, n+1):
        if i*j <= n:
            cnt += 1

print(cnt)
# 예시인 6의 경우 1x1 ~ 1x6까지 있고 2는 2x2, 2x3이 있으므로 8개.
# 즉 1부터 6까지 자기보다 크거나 같은 숫자들만 곱해보면서 주어진 숫자보다 작거나 같으면 해당 개수의 정사각형으로 만들 수 있는 직시각형이 나옴.
