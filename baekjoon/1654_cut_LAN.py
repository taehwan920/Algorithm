k, n = map(int, input().split())
lan = []
for i in range(k):
    lan.append(int(input()))
start, end = 0, max(lan)
result = 0
while start <= end:
    mid = (start + end) // 2 if (start + end) // 2 != 0 else 1
    cnt = 0
    for i in lan:
        cnt += i // mid
    if cnt >= n:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)

# 갖고있는 K개를 잘라 N개 이상의 랜선으로 만들고 싶은 문제
# 최소값은 0, 최대값은 갖고있는 랜선 중 가장 긴 길이로 설정.
# 각 랜선 별로 mid의 길이대로 잘라서 mid보다 길거나 같게나온 랜선만 카운팅 하기 위해 각 랜선을 mid로 나눈 몫을 카운팅.
# 카운팅한 랜선이 갖고자 하는 랜선 수보다 많을 경우 최소값을 mid보다 1크게 설정. 아닐 경우 최대값을 mid보다 1작게 설정.
# 갖고있는 랜선 수 1, 갖고자 하는 랜선 수 1일 경우 mid값이 0이 나와버려서 0나누기 런타임 에러가 떠서 mid값 설정을 위와같이 함.
