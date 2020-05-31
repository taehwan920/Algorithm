N, C = map(int, input().split())

house = []

for i in range(N):
    house.append(int(input()))

house.sort()

start = house[1] - house[0]
# 구해야하는게 공유기 설치 폭이기 때문에 주어진 배열 내 가장 작은 공유기 설치폭을 구함 (min)
end = house[-1] - house[0]
# 주어진 배열 내 가장 큰 공유기 설치 폭(max)
result = 0

while start <= end:
    # 앞으로 점점 min과 max의 차이를 줄여나가며 진행할 것이기 때문에 while 유지 조건을 이렇게 설정.
    mid = (start + end) // 2
    # 공유기 설치폭의 최소/최대값의 중간값(정수) 설정
    value = house[0]
    # 첫 집 선택
    count = 1
    # 첫 집은 무조건 깔고 들어가므로 count 변수도 1을 디폴트로.
    for i in range(1, len(house)):
        if house[i] >= value + mid:
            # 두번째 집부터 보는데, 바로 직전 집에서 mid값을 더한 거리보다 멀면 설치한다
            count += 1
            value = house[i]
            # 다음 연산 때 쓸 현재 집을 저장

    if count >= C:
        # 공유기 설치 대수가 주어진 것과 같거나 그보다 클때
        start = mid + 1
        # min값을 mid보다 1 크게해줌. 왜냐면 mid는 이미 연산에 사용되었으니 범위를 제대로 좁히려면 mid보다 1 더 큰값으로 해줘야 하기 때문.
        result = mid
        # 일단 결과값에는 현재 mid값을 저장.
    else:
        end = mid - 1
        # 만약 설치된 공유기가 주어진 것보다 적게 설치 되었으면 마찬가지로 탐색 범위를 좁히기 위해 end값을 mid보다 1작게 설정해준다.
print(result)
