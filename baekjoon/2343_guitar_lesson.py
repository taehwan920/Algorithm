n, m = map(int, input().split())
lesson = list(map(int, input().split()))

start = 0
end = sum(lesson)
result = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    total_minute = 0
    for i in range(len(lesson)):
        if total_minute + lesson[i] <= mid:
            total_minute += lesson[i]
        else:
            total_minute = lesson[i]
            cnt += 1
    if cnt <= m:
        end = mid - 1
    else:
        start = mid + 1
        result = start

    # print('s', start, 'e', end, 'cnt', cnt)
MAX = max(lesson)
result = result if result >= MAX else MAX
print(result)


# 오랜만에 푼 이분 탐색 문제.
# 기본적인 이분탐색문제들이 다 그렇듯이 start값, end값, mid값, cnt값을 뭘로 설정할지만 명확하게 설정하면 나머지는 알고리즘에 따라 코드를 작성하는 것 뿐이다.
# 처음 이 문제를 봤을때는 그냥 기계적으로 0과 주어진 배열의 끝값을 start와 end로 잡고 하려고 했으나 그러면 mid값이 너무 작아져서 배열의 가장 큰값마저 담을 수 없게 돼서 이상함을 느끼고 전략을 수정했다.
# 그래서 이 문제가 구하고자 하는 답은 비디오의 총 길이이므로 start는 0으로, end는 lesson 배열의 총 합으로 잡기로 했다.
# 그래서 반복문을 돌며 mid값 길이의 비디오에 들어갈 만큼 레슨을 넣고, 레슨이 더이상 안들어가는 크기면 사용 비디오 개수 cnt를 하나 늘리고 누적 비디오 길이인 total_minute를 0으로 만드는 식으로 새 비디오에 넣는 걸 구현했다.
# 그렇게 얻은 비디오 개수가 만약 m보다 작거나 같으면 비디오 당 최대 길이를 짧게 만들어 비디오 개수를 늘려야하므로 mid 크기를 줄여야 함. 즉 end를 mid - 1로 만들고
# 만약 m 보다 크다면 비디오당 최대 길이를 길게 만들어 비디오 개수를 줄여야하므로 한 비디오의 최대 길이인 mid를 늘려야함. 즉 start를 mid + 1로 만든다.
# 예외 사항으로 이분탐색으로 구한 m개의 비디오에 모든 레슨을 나눠담을 수 있는 비디오 길이 중 가장 짧은 길이인 result가
# lesson 배열의 최대값, 즉 가장 긴 강의 영상 하나의 길이보다 짧다면 답이 성립하지 않으므로(강의를 모두 담아야함)
# 만약 lesson 배열 내 최대값보다 구한 비디오 길이가 짧다면 답을 배열의 최대값으로 설정해주면 된다.
